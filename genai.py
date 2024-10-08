
import google.generativeai as genai
import os
import pandas as pd
from PyPDF2 import PdfReader
import json
import psycopg2
from sqlalchemy import create_engine
from tabulate import tabulate

genai.configure(api_key="AIzaSyBTtPfm20WiKRPqxbmCTeHkw5pGSTqjfjo")
model = genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config={"response_mime_type": "application/json"})
reader = PdfReader('resume.pdf')
no_of_pages = len(reader.pages)
for pg in range(0,no_of_pages):
    page = reader.pages[pg]
    text = page.extract_text()
response = model.generate_content(f" {text} You are a best resume Extractor where you will be screening the resumes and find the name, college, email, phone number and skills n skills remove colon and text before colon don't give skills as list. give each skill in a new line print long text in new line in the same column. give json format")
dt = response.text
# print(type(dt))
dd = json.loads(dt)
#print(dd)

conn_string = 'postgresql://postgres:post123@localhost/gendb'
database = create_engine(conn_string)
conn = database.connect()
df =  pd.DataFrame([dd])
#print(df)
#print(tabulate(df, headers='keys', tablefmt='psql))
df.to_sql('mytab', con=conn, if_exists='replace', index=False) 
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
sql1 = '''select * from mytab;'''
cursor.execute(sql1)
res = cursor.fetchall()
out = pd.DataFrame(res)
print(tabulate(out, headers='keys', tablefmt='psql'))
#print("Connected to database")
conn.commit() 
conn.close()









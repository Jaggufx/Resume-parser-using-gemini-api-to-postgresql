# Resume-parser-using-gemini-api-to-postgresql

**Description**
This project utilizes Google Generative AI to extract structured information from resumes in PDF format.
It processes the content of a resume to identify and retrieve the candidate's name, college, email, phone number, and skills.

Install python

**Modules required**
- import google.generativeai as genai
- import os
- import pandas as pd
- from PyPDF2 import PdfReader
- import json
- import psycopg2
- from sqlalchemy import create_engine
- from tabulate import tabulate

Gemini API: https://ai.google.dev/

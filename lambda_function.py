import boto3
import io
import os
import base64
from docx import Document
from docx.shared import Inches
from fpdf import FPDF
from io import BytesIO

def lambda_handler(event, context):

    print("event['body'] : " + event['body'])

    demo_file = base64.b64decode(event['body'])

    docx_bytes = demo_file
    
    print('docx_bytes : ' + str(docx_bytes))
    pdf_bytes = convert_docx_bytes_to_pdf(docx_bytes)
    
    print('pdf_bytes : ' + str(pdf_bytes))

    #pdf_bytes = convert_docx_to_pdf(demo_file)

    s3_bucket = 'filestore-piyush08'
    s3_key = 'output.pdf'
    upload_to_s3(pdf_bytes, s3_bucket, s3_key)

    return {
        'statusCode': 200,
        'body': 'File converted and uploaded successfully to S3.'
    }

def convert_docx_to_pdf(docx_file):
    doc = Document(io.BytesIO(docx_file))

    pdf = FPDF()

    for para in doc.paragraphs:
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, para.text, ln=True)

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)

    return pdf_output.getvalue()

def upload_to_s3(file_bytes, bucket, key):
    s3 = boto3.client('s3')

    s3.put_object(Body=file_bytes, Bucket=bucket, Key=key)
def convert_docx_bytes_to_pdf(docx_bytes):
    docx_io = BytesIO(docx_bytes)
    
    print('docx_io : ' + str(docx_io))

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(40, 10, txt="Hello, World!", ln=1)
    pdf_bytes = pdf.output(dest='S')

    return pdf_bytes


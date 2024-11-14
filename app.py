from flask import Flask, render_template, request, redirect, url_for
from transformers import pipeline
import os

app = Flask(__name__)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for uploading PDFs
@app.route('/upload', methods=['GET', 'POST'])
def upload_pdf():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        if pdf_file:
            # Save the uploaded file
            file_path = os.path.join('uploads', pdf_file.filename)
            pdf_file.save(file_path)
            
            # Process the PDF (this should include reading and summarizing the PDF)
            summary = "Summary of the PDF will go here."
            
            # Render the results page with the summary
            return render_template('results.html', summary=summary)
        else:
            return render_template('upload.html', error="No file part")
    
    return render_template('upload.html')

# Route for displaying results
@app.route('/results')
def results():
    # Here, you should return the results of the PDF summarization
    return render_template('results.html', summary="Summary will appear here.")

if __name__ == '__main__':
    app.run(debug=True, port = 6969)

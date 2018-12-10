FROM tiangolo/uwsgi-nginx-flask:python3.6
# Install spaCy.io
RUN pip install -U spacy
RUN python -m spacy download en

EXPOSE 5000
CMD ["python", "/app/main.py"]
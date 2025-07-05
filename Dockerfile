FROM python:3.8
ADD . /devops/test
WORKDIR /devops/test
RUN pip install -r requirements.txt
CMD ["python", "currency_converter.py"]
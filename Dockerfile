FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
COPY src /src
WORKDIR /src
RUN pip install --upgrade pip && pip install -U -r requirements.txt
CMD bash -c "python3 main.py"
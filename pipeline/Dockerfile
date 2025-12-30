#install python dependencies
FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:${PATH}"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked


#install lybraries we need
#RUN pip install pandas pyarrow

#create the working library and the container


#copy the pipeline code into the container
COPY pipeline.py .

#specify the command to run on container startup ()par exemple python3 pipeline.py)
ENTRYPOINT ["python", "pipeline.py"]
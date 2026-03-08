FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir .

CMD ["mcp-flux-pro", "--transport", "http", "--port", "8000"]

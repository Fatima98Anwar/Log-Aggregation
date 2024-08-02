from flask import Flask, request
import logging
import os

from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk.resources import Resource
from opentelemetry._logs import set_logger_provider
from dotenv import load_dotenv

load_dotenv()

OTEL_EXPORTER_OTLP_ENDPOINT = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://otel-collector:4317")

logger_provider = LoggerProvider(
    resource=Resource.create(
        {
            "service.name": "flask-dummy",
            "service.instance.id": os.uname().nodename,
        }
    ),

)
set_logger_provider(logger_provider)

otlp_exporter = OTLPLogExporter(endpoint=OTEL_EXPORTER_OTLP_ENDPOINT, insecure=True)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(otlp_exporter))

handler = LoggingHandler(level=logging.DEBUG, logger_provider=logger_provider)

logging.getLogger().addHandler(handler)
logger = logging.getLogger("flask-dummy")

logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/get')
def get():
  logger.warning("Received GET request")
  return {'success': True}

@app.route('/post', methods = ["POST"])
def post():
  logger.info("Received POST request")
  return {'success': True}
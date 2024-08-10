import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# here we mention the module in logging which main.py

log_dir = "logs"
log_filepath = os.path.join(log_dir,"ml_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # it will create  log folder
        logging.StreamHandler(sys.stdout) # it will print the log in terminal
    ]
)

logger = logging.getLogger("mlLogger")
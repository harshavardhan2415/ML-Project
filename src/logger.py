import logging
import os
from datetime import datetime

# Step 1: Create logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Ensure 'logs' directory exists

# Step 2: Create log file name with timestamp
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 3: Full path to the log file
log_file_path = os.path.join(logs_dir, log_file)

# Step 4: Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Step 5: Write a log message
if __name__ == "__main__":
    logging.info("Logging has started")
    print(f"Log file created at: {log_file_path}")

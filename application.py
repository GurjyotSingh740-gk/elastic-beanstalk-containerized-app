import logging
import os
from flask import Flask, render_template

application = Flask(__name__)

# Configure centralized standard out logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DockerPortfolioApp")

@application.route('/')
def index():
    logger.info("Portfolio landing page evaluated and served successfully.")
    return render_template('index.html')

@application.route('/health')
def health():
    # Dedicated low-overhead verification endpoint for AWS target groups
    return "OK", 200

if __name__ == "__main__":
    # Pull dynamic allocation port from environment variables, or fallback to 5000
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port)
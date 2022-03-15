import sys
import logging
import logging.config
from src.utils import conf_folder

logging.config.fileConfig(conf_folder('logging.conf'))
log = logging.getLogger(__name__)

def main(args):
    log.info("Imports complete, program starting...")
    log.info(args)
    return True

if __name__ == "__main__":
    main(sys.argv[1:])
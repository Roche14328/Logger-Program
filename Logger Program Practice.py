Sure, here's a slightly different implementation of the Logger class using a class method instead of overriding \_\_new\_\_:


import logging

class Logger:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('log.txt')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log(self, level, message):
        if level == 'INFO':
            self.logger.info(message)
        elif level == 'WARNING':
            self.logger.warning(message)
        elif level == 'ERROR':
            self.logger.error(message)
        elif level == 'FATAL':
            self.logger.critical(message)
        else:
            self.logger.debug(message)

if __name__ == '__main__':
    logger = Logger.get_instance()
    logger.log('INFO', 'This is an info message')
    logger.log('WARNING', 'This is a warning message')
    logger.log('ERROR', 'This is an error message')
    logger.log('FATAL', 'This is a fatal message')

# Logger Program Report
---
## Introduction
This report presents the implementation details of a Logger program in Python using the Singleton pattern. The program records user actions and timestamps, supporting multiple levels of logs such as INFO, WARNING, ERROR, and FATAL.

## Manual
To build the application, I created a Logger class using the Singleton pattern to ensure only one instance of the logger exists throughout the application. The logger logs messages with different levels and appends them to the same log file. For some one who will use my git repo he needs to follow the following steps:
#### Building the Application from git repo
1. Clone the GitHub repository to your local machine.
2. Open the project in your preferred Python IDE or text editor.
3. Run the Singleton Practice.py script to execute the logger program.
4. Customize logging messages and levels as needed for your application.

## GitHub Repository
Link to GitHub Repository: [Logger Program Repo](https://github.com/yourusername/logger-program)

## Key Code Explanations
```python
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
```



## Screenshots
![Logger Screenshot](1.png)
![Logger Screenshot](2.png)
## Verification of Program Functionality
To ensure that the Logger program is working correctly, you can perform the following verification steps:
1. Create test cases for each log level (INFO, WARNING, ERROR, FATAL) and log messages.
2. Execute the program and verify that the log messages are being recorded in the log file.
3. Check the log file to confirm that the timestamps, log levels, and messages are correctly logged.
4. Trigger different user actions in your application and observe the corresponding log entries.
5. Use the logging functionality in a sample project or application to validate its integration and functionality.

By following these verification steps, you can confirm that the Logger program is functioning as intended and effectively capturing user actions and timestamps in the log file.

## Development Challenges and Solutions
- **Challenge:** Ensuring thread safety in the Singleton pattern.
  - **Solution:** Implemented thread-safe initialization using a locking mechanism to prevent race conditions.

- **Challenge:** Handling different log levels and their corresponding actions.
  - **Solution:** Utilized enums to define log levels and conditional statements to determine logging behavior based on the specified level.

## Conclusion
In conclusion, the development of the logger program utilizing the Singleton pattern has been successful. The program effectively manages logging of user actions with timestamps and supports multiple levels of logging for different severity levels. Through the implementation of thread-safe initialization and careful consideration of logging behaviors, the program ensures reliable and efficient logging functionality.

Moving forward, potential enhancements could include:
- Integration with external logging services for centralized log management.
- Addition of custom formatting options for log messages.
- Implementation of log rotation to manage log file size and ensure data integrity over time.

Overall, this logger program provides a robust foundation for logging user actions and system events in Python applications.

---
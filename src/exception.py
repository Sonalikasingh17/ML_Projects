import sys
from src.logger import logging

# def error_exit(message: str, code: int = 1) -> None:
#     """
#     Print an error message to stderr and exit the program with the given exit code.
    
#     :param message: The error message to print.
#     :param code: The exit code to use when exiting the program.
#     """
#     print(f"Error: {message}", file=sys.stderr)
#     sys.exit(code)

def error_message_detail(error,error_detail:sys):
    """
    This function is used to format the error message with details.
    
    :param error: The error object.
    :param error_detail: The sys module to access the exc_info method.
    :return: A formatted string containing the error message and details.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    # error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    #     file_name, exc_tb.tb_lineno, str(error))
    
    # return error_message
    line_number = exc_tb.tb_lineno
    return f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"

class CustomException(Exception):
    """
    Custom exception class to handle exceptions with detailed error messages.
    
    :param error: The error object.
    :param error_detail: The sys module to access the exc_info method.
    """
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":

    try:
        raise ValueError("An example error")
    except Exception as e:
        logging.basicConfig(level=logging.ERROR)
        logging.error(CustomException(e, sys))
        print(CustomException(e, sys))  # This will print the formatted error message
   
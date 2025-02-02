import re

def clean_data_from_file(file_path):
    """
    Reads a text file and extracts all valid decimal numbers from it.
    
    A token (word) from the file is only considered a valid number if the entire token matches one
    of the following formats:
        - An integer, e.g., "42", "-17", "+3"
        - A floating-point number with a decimal point, e.g., "3.14", "-0.001", ".5", "+.75"
        
    Any token that does not exactly match these formats (even if it begins with a valid number)
    is ignored.
    
    Parameters:
        file_path (str): The path to the input text file.
    
    Returns:
        list of float: A list of numbers extracted from the file.
    """
    # This regular expression matches a complete token representing a decimal number.
    # Breakdown:
    #   [+-]?              -> Optional sign
    #   (?:\d*\.\d+|\d+)   -> Either a floating-point number (allowing an optional integer part)
    #                        or an integer.
    number_pattern = re.compile(r'[+-]?(?:\d*\.\d+|\d+)')
    
    numbers = []
    
    with open(file_path, 'r') as file:
        # Split the file into tokens based on whitespace.
        tokens = file.read().split()
    
    # Check each token to see if it exactly matches our number pattern.
    for token in tokens:
        # fullmatch ensures the entire token is a valid number.
        if number_pattern.fullmatch(token):
            numbers.append(float(token))
    
    return numbers

# Example usage:

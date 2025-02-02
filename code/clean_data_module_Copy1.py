import re

def clean_data_from_file(file_path):
    """
    Reads a text file and extracts all decimal numbers from it.

    The file is assumed to contain numbers in decimal format (e.g., 3.14, -2.718, 42)
    interspersed with other text. Any word that does not represent a valid decimal number
    is ignored.

    Parameters:
        file_path (str): The path to the input text file.

    Returns:
        list of float: A list of numbers extracted from the file.
    """
    # This regular expression matches:
    # - Optional sign (+ or -)
    # - Either:
    #   a) A floating-point number with a decimal point (digits may appear before the point)
    #      e.g., -3.14, .5, +0.001
    #   b) An integer number
    # The pattern is: sign? (digits*.digits+ | digits+)
    pattern = r'[-+]?(?:\d*\.\d+|\d+)'
    
    # Open and read the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Find all substrings in the content that match the number pattern.
    matches = re.findall(pattern, content)
    
    # Convert all found matches to floats.
    numbers = [float(match) for match in matches]
    
    return numbers



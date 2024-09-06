def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Ensure the input string is not empty or contains leading/trailing spaces
    if not txt.strip():
        return False
    
    # Extract the last character and remove it from the string
    last_char = txt.strip()[-1]
    txt_without_last = txt[:-1]
    
    # Split the string into individual words using space as delimiter
    words = txt_without_last.split()
    
    # Check if the last character is part of a word or not
    return last_char not in words and last_char.isalpha()
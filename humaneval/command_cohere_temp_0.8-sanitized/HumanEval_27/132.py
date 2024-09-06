def flip_case(string: str) -> str:
    """
    Flip case of characters in a string. Turn lowercase characters to uppercase and uppercase characters to lowercase.
    
    Parameters:
    string (str): Input string to modify.

    Returns:
    str: The modified string with flipped case.
    """
    # Use a list comprehension to iterate each character in the string.
    modified_string = list(string)
    for char in modified_string:
        # If the character is lowercase, make it uppercase.
        if char.islower():
            modified_string[modified_string.index(char)] = char.upper()
        # If the character is uppercase, make it lowercase.
        elif char.isupper():
            modified_string[modified_string.index(char)] = char.lower()
    # Convert the modified list back to a string and return.
    return ''.join(modified_string)
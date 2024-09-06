def flip_case(string: str) -> str:
    """
    Flip case of characters in a string. Turn lowercase characters to uppercase and uppercase characters to lowercase.
    """
    # Iterate through each character in the string
    result = ''
    for char in string:
        # If the character is lowercase, make it uppercase
        if char.islower():
            result += char.upper()
        # If the character is uppercase, make it lowercase
        elif char.isupper():
            result += char.lower()
        # Keep the character as it is for any other case
        else:
            result += char
    return result
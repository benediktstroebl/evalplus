def flip_case(string: str) -> str:
    """
    Flip lowercase characters to uppercase and uppercase characters to lowercase in a string.
    :param string: String to transform.
    :return: The modified string.
    """
    modified = ""
    for char in string:
        if char.islower():
            modified += char.upper()
        elif char.isupper():
            modified += char.lower()
        else:
            modified += char
    return modified
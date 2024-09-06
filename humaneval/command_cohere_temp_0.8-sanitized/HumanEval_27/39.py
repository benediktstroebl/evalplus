def flip_case(string: str) -> str:
    """
    Flip uppercase characters to lowercase and lowercase characters to uppercase.
    """
    flipped_string = ''
    for char in string:
        if char.isupper():
            flipped_string += char.lower()
        elif char.islower():
            flipped_string += char.upper()
        else:
            flipped_string += char
    return flipped_string
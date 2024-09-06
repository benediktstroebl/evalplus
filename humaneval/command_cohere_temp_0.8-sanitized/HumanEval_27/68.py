def flip_case(string: str) -> str:
    """
    Flip uppercase characters to lowercase and lowercase characters to uppercase.
    """
    flipped = ''
    for char in string:
        if char.isupper():
            flipped += char.lower()
        elif char.islower():
            flipped += char.upper()
        else:
            flipped += char
    return flipped
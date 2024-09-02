

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Convert the string to uppercase
    uppercase = string.upper()

    # Iterate through each character and flip its case
    for char in uppercase:
        if char.islower():
            yield char.upper()
        elif char.isupper():
            yield char.lower()
        else:
            yield char
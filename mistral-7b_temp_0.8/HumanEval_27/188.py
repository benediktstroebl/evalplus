

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # YOUR CODE HERE
    new_string = ""
    for character in string:
        if character.isupper():
            character = character.lower()
        else:
            character = character.upper()
        new_string += character

    return new_string




def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # TODO: Write a unit test for this function.

    # Choose the upper() or lower() function depending on the case of the first letter.
    return (
        (string[0].lower(), string.lower()[1:])
        if string[0].isupper()
        else (string[0].upper(), string.upper()[1:])
    )


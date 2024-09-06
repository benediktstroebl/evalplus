

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    lower_characters = [char for char in string if char.islower()]
    upper_characters = [char for char in string if char.isupper()]
    flip_lower_characters = [char.swapcase() for char in lower_characters]
    flip_upper_characters = [char.swapcase() for char in upper_characters]
    lower_characters += flip_upper_characters
    upper_characters += flip_lower_characters
    return "".join(lower_characters + upper_characters)


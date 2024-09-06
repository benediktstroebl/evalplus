

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lower_string = string.lower()
    upper_string = string.upper()
    combined_string = lower_string + upper_string
    flipped_string = "".join(sorted(combined_string))
    return flipped_string

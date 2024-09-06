

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # TODO: Your solution here
    string_split = list(string)
    for i in range(0, len(string_split)):
        if string_split[i].isupper():
            string_split[i] = string_split[i].lower()
        elif string_split[i].islower():
            string_split[i] = string_split[i].upper()
    return "".join(string_split)


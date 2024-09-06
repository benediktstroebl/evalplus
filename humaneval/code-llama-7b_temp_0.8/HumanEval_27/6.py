

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # Split the string into a list of single-character strings.
    str_split = list(string)

    # Iterate over each character.
    for i, letter in enumerate(str_split):
        # Convert the character to uppercase.
        if letter.islower():
            str_split[i] = str_split[i].upper()
        # Convert the character to lowercase.
        else:
            str_split[i] = str_split[i].lower()

    # Join the list of single-character strings back into a string.
    return "".join(str_split)



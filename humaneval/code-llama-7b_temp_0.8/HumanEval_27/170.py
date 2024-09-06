

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # First, check if any letters are flippable.
    # If not, just return the string.
    for letter in string:
        if letter.islower():
            break
    else:
        return string

    # If we get this far, at least one letter is flippable.
    # Make a new empty string to store our results
    new_string = ""

    # Use enumerate to keep track of the index.
    # If the character is lowercase, change it to uppercase
    for index, letter in enumerate(string):
        if letter.islower():
            letter = letter.upper()
        # If the character is uppercase, change it to lowercase
        elif letter.isupper():
            letter = letter.lower()
        new_string += letter

    return new_string


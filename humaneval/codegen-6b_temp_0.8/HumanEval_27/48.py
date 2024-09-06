

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # for letter in string:
    #     if letter.isupper():
    #         flipped_letter = letter.lower()
    #     else:
    #         flipped_letter = letter.upper()
    #     print(letter, flipped_letter)
    # return string
    return string.swapcase()


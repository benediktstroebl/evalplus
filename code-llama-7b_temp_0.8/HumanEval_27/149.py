

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # approach 1 - the only way I could get this to work
    new_string = ''
    for letter in string:
        if letter.islower():
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    return new_string


    # # approach 2
    # new_string = ''
    # for letter in string:
    #     if letter.islower():
    #         new_string += letter.upper()
    #     else:
    #         new_string += letter.lower()
    # return new_string


    # # approach 3
    # new_string = ''
    # for letter in string:
    #     new_string += letter.upper() if letter.islower() else letter.lower()
    # return new_string



    # # approach 4
    # return string.swapcase()

    # # approach 5
    # return string.lower().swapcase()





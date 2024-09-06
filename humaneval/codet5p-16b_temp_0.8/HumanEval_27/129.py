

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    flipped_string = ''
    for i in string:
        if i.isupper():
            flipped_string += lower_case[upper_case.find(i)]
        elif i.islower():
            flipped_string += upper_case[lower_case.find(i)]
        else:
            flipped_string += i
    return flipped_string


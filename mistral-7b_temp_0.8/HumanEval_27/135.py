

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # your code here
    if string == '':
        return 'Empty string'
    else:
        final_string = ''
        for char in string:
            if char.isupper():
                final_string += char.lower()
            elif char.islower():
                final_string += char.upper()
            else:
                final_string += char
        return final_string


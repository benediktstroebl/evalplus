

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = list(string)
    for index, letter in enumerate(string):
        if letter.isupper():
            string[index] = letter.lower()
        elif letter.islower():
            string[index] = letter.upper()

    return ''.join(string)

assert flip_case('Hello') == 'hELLO'
assert flip_case('SUNDAY') == 'SuNdAy'
assert flip_case('APPLE') == 'ApplE'
assert flip_case('-EXAMPLE-') == 'eXaMpLe'
assert flip_case('12345') == '12345'
assert flip_case('AbCdEfG') == 'ABCDEFG'
assert flip_case('hello') == 'hELLO'

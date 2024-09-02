

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string_length = len(string)
    flipped_string = ''
    for index in range(0, string_length):
        if string[index].isupper():
            flipped_string += string[index].lower()
        else:
            flipped_string += string[index].upper()
        if index == string_length - 1:
            flipped_string += string[index]
    return flipped_string

assert flip_case('Hello') == 'hELLO'
assert flip_case('HELLO') == 'hello'
assert flip_case('apple') == 'aPpLe'
assert flip_case('Apple') == 'aPpLe'
assert flip_case('asdfg') == 'zdfgAs'
assert flip_case('Asdfg') == 'zdfgAs'
assert flip_case('Hello World') == 'hELLO wORLD'
assert flip_case('KLJFJFJF') == 'KKJFFFJ'
assert flip_case('KJFJFJF') == 'KKJFFFJ'
assert flip_case('klfjdfl') == 'lklfjdfl'
assert flip_case('klfjdfl') == 'lklfjdfl'
assert flip_case('klfjdklfjdfl') == 'lklfjdklfjdfl'
assert flip_case('klfjdklfjdl') == 'lklfjdklfjdl'
assert flip_case('HelloWorld') == 'HelloWorld'


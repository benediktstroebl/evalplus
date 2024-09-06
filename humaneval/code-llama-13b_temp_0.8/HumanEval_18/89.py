

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if string == '' or substring == '':
        return 0

    substr_size = len(substring)
    str_size = len(string)
    number_of_substr = 0

    for i in range(str_size - substr_size + 1):
        if string[i:i+substr_size] == substring:
            number_of_substr += 1

    return number_of_substr


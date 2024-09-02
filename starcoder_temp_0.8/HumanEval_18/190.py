

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    
    if not substring:
        return 0

    counter = 0
    for index in range(len(string)):
        if string[index] == substring[0]:
            counter += 1
            if len(substring) > 1:
                if not substring[1:] in string[index + 1:]:
                    counter -= 1

    return counter

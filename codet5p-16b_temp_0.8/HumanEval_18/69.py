

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    counter = 0
    index = 0
    while index < len(string):
        if string[index] == substring[0] and index + len(substring) <= len(string):
            found = True
            for i in range(len(substring)):
                if string[index + i]!= substring[i]:
                    found = False
            if found:
                counter += 1
        index += 1
    return counter


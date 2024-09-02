

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # To avoid creating unused variables, I use the variables `result` and `times` outside the function.
    result = 0
    times = 0
    # Loop through the string backwards, to prevent out of bounds.
    # https://docs.python.org/3/library/functions.html#xrange
    for i in range(len(string) - len(substring), -1, -1):
        if string[i: i + len(substring)] == substring:
            result += 1
            times += 1
        elif string[i - 1] != ' ':
            break
    return result


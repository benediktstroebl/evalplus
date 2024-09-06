

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if string == "" or substring == "":
        return 0
    count = 0
    last_i = 0
    while last_i < len(string):
        i = string.find(substring, last_i)
        if i == -1:
            return count
        else:
            count += 1
            last_i = i+1
    return count

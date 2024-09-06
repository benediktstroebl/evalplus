

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # find all occurances of the substring in the string
    # iterate through the matches and add them to a new list
    # return the length of the new list
    return len([s for s in re.finditer(substring, string)])

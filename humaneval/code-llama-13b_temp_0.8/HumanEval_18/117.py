

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # Make sure both string and substrings are not empty
    if not string or not substring:
        return 0

    # If a substring is longer than a string, there can be no occurence
    if len(substring) > len(string):
        return 0

    # Find the first occurence, if any
    first_index = string.find(substring)

    # No occurence found
    if first_index == -1:
        return 0

    # Find all the rest
    rest = string[first_index+1:]

    # If there are none, return 1, otherwise add 1 and recurse
    return 1 + how_many_times(rest, substring)


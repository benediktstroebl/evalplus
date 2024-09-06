

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # 1. Ask for permission
    if not isinstance(string, str):
        raise TypeError(f"'{string}' is not a valid string")
    if not isinstance(substring, str):
        raise TypeError(f"'{substring}' is not a valid string")
    # 2. Check conditions
    if len(string) == 0:
        return 0
    if len(substring) == 0:
        raise ValueError('The substring can not be empty')
    # 3. Compute
    count = 0
    while True:
        try:
            start = string.index(substring)
        except ValueError:
            return count
        count += 1
        string = string[start+1:]


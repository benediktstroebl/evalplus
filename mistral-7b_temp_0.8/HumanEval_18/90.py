

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not string or not substring:
        return 0

    if len(substring) > len(string):
        return 0

    # Use the index of the first character of the substring as a sliding window
    # and increment it until it equals the length of the substring.
    first_char = string.find(substring[0], 0)
    count = 0

    while first_char != -1:
        # If the remaining substring of the original string starts with the
        # same character as the first character of the substring, increment the
        # count and move the first character index.
        if string[first_char + len(substring)] == substring[0]:
            count += 1
            first_char = string.find(substring[0], first_char + len(substring))
        else:
            first_char = string.find(substring[0], first_char + 1)

    return count

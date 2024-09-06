

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if len(string) == 0:
        return 0

    if len(substring) == 0:
        return 0

    if len(string) < len(substring):
        return 0

    string_length = len(string)
    substring_length = len(substring)

    # Replace substring with a character
    repl_substring = substring[0] + substring[0] * (substring_length - 2)

    count = string.count(repl_substring)

    # Backtrack
    for i in range(string_length - substring_length):
        if string[i:i + substring_length] == substring:
            count -= 1

    return count



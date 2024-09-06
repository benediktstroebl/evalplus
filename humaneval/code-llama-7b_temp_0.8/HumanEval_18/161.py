

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    length_of_substring = len(substring)
    length_of_string = len(string)

    if length_of_string < length_of_substring:
        return 0
    else:
        for i in range(0, length_of_string - length_of_substring + 1):
            if string[i:i + length_of_substring] == substring:
                count += 1

        return count


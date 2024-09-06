

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    length = len(string)
    substring_length = len(substring)
    count = 0
    if substring_length == 0 or length == 0 or substring_length > length:
        return 0

    for i in range(length):
        for j in range(substring_length):
            if string[i+j]!= substring[j]:
                break
            elif j == substring_length - 1:
                count += 1

    return count

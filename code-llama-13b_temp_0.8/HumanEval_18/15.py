

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
    for i in range(len(string)):
        if string[i] == substring[0]:
            substring_length = len(substring)
            substring_pos = i
            if len(string) - i < len(substring):
                substring_length = len(string) - i
            for j in range(substring_length):
                if string[i + j] != substring[j]:
                    break
            else:
                count += 1
    return count


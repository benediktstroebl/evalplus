

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
    i = 0
    while i < len(string) and substring[i] == string[i]:
        i += 1
        count += 1
    return count

def count_a_of_b(a: str, b: str) -> int:
    """ Count the number of As in the string b, assuming that all As in b are preceded and followed by Bs.
    >>> count_a_of_b('aaabbb', 'bbb')
    2
    >>> count_a_of_b('aaabbb', 'aa')
    0
    >>> count_a_of_b('aaabbb', 'aab')
    1
    """
    i = 0
    count = 0
    while i < len(b):
        if b[i] == 'B':
            i += 1
        elif b[i] == 'A':
            count += 1
        i += 1
    return count
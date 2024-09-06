

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
    position = 0
    while position < len(string) - len(substring):
        substring_found = False
        for j, letter in enumerate(string[position:]):
            if letter == substring[j]:
                count += 1
                position += j + 1
                substring_found = True
                break
        if not substring_found:
            break
    return



def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # 1. count the number of substring in the string
    # 2. check if the substring is present in the original string
    # 3. count how many times the substring is found
    # 4. return the count
    count = 0
    for i in range(0, len(string) - len(substring) + 1):
        if string[i : i + len(substring)] == substring:
            count += 1
    return count


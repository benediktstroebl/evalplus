

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    count = 0
    if len(string) == 0:
        return 0
    else:
        count = 1
        string = string.lower()
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                pass
            else:
                count += 1
    return count


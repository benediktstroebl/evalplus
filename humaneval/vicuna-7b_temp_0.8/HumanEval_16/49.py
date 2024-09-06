

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = str(string)
    count = len(string)
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i] != string[j]:
                count -= 1
                break
    return count

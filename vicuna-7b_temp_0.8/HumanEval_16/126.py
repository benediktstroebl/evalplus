

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if string is None or string == "":
        return 0
    string = string.lower()
    n = len(string)
    distinct = 0
    for i in range(n):
        for j in range(i + 1, n):
            if string[i] != string[j]:
                distinct += 1
        if string[i] == string[j]:
            distinct += 1
    return distinct



def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    def count_chars(s):
        d = {}
        for char in s:
            if char.lower() not in d:
                d[char.lower()] = 1
            else:
                d[char.lower()] += 1
        return d.values()
    return sum(count_chars(s) for s in string.split())


def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # SOLUTION 1
    #  O(n log n) time, O(1) space
    # return len(set(string.lower()))

    # SOLUTION 2
    # O(n) time, O(1) space
    # chars = [False] * 256
    # count = 0
    # for c in string:
    #     index = ord(c)
    #     if not chars[index]:
    #         chars[index] = True
    #         count += 1
    # return count

    # SOLUTION 3
    # O(n) time, O(n) space
    chars = set()
    for c in string:
        chars.add(c.lower())
    return len(chars)


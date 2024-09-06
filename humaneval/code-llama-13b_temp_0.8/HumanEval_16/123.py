

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # count = 0
    # for c in string:
    #     if c.islower():
    #         count += 1
    #     elif c.isupper():
    #         count += 1
    # return count

    # count = 0
    # distinct_letters = []
    # for c in string:
    #     if c.lower() not in distinct_letters:
    #         distinct_letters.append(c.lower())
    #         count += 1
    # return count

    # set comprehension
    return len({c.lower() for c in string})

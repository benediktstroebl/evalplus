

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # return 0

    # res = []
    # for char in string:
    #     if char.lower() not in res:
    #         res.append(char.lower())
    # return len(res)

    # return 0

    # return len(set(string.lower()))

    # return len(set(string.lower()) & set(string.upper()))

    # return 0

    # lower_chars = [char.lower() for char in string]
    # return len(set(lower_chars))

    # return 0

    # return len(set(string.lower()) | set(string.upper()))

    # return len({char for char in string.lower()})

    return len(set(string.lower()))


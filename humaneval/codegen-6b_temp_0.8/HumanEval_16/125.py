

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    lowercase = set()
    uppercase = set()
    for ch in string:
        if ch.isalpha():
            if ch.isupper():
                uppercase.add(ch)
            else:
                lowercase.add(ch)
        else:
            continue

    return len(lowercase) + len(uppercase)

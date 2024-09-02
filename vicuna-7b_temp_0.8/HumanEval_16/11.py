

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_chars = set()
    for char in string:
        if char.lower() not in distinct_chars:
            distinct_chars.add(char.lower())
    return len(distinct_chars)

if __name__ == '__main__':
    string = input("Enter a string: ")
    print(count_distinct_characters(string))
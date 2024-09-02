

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    distinct_count = 0
    for i in range(len(string)):
        for j in range(len(string) - i):
            current_character = string[j:j + 1].lower()
            if current_character in string[j + 1:j + i + 2]:
                distinct_count += 1
                break

    return distinct_count


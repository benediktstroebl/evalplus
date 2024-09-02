

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # time: O(n); space: O(n)
    lower_string = string.lower()
    return len(set(lower_string))

    # time: O(n*log(n)); space: O(1)
    # string = sorted(string)
    # distinct_count = 0
    # for i in range(1, len(string)):
    #     if string[i] != string[i - 1]:
    #         distinct_count += 1
    # return distinct_count + 1


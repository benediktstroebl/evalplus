

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    final_list = []
    for letter in string:
        if letter not in final_list:
            final_list.append(letter)
    print(len(final_list))


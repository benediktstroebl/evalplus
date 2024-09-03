def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    letters_dict = {letter: None for letter in string.lower()}
    for letter in string.lower():
        if letters_dict[letter] is None:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    return len(letters_dict)

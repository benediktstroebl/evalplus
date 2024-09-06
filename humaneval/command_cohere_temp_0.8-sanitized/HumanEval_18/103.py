def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.

    :param string: Original string
    :param substring: Substring to search for
    :return: Number of times substring occurs in string
    :raises ValueError: If substring is empty
    """
    if not substring:
        raise ValueError("Empty substring is not allowed")
    
    count = 0
    temp_string = string.copy()
    temp_substring = substring.copy()
    
    while temp_string and temp_substring:
        if temp_string[0] == temp_substring[0]:
            count += 1
            temp_string = temp_string[1:]
            temp_substring = temp_substring[1:]
        else:
            temp_string = temp_string[1:]
    return count
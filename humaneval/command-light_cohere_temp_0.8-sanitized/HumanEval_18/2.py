def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string.

    :overlapping substring instances are counted  
    Return 0 if the substring is not found anywhere 
    """
    return sum(1 for _ in string.contains(substring))
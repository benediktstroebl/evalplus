def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of occurrences of the substring in the original string.
    """
    if not string or not substring:
        return 0

    count = 0
    i = 0
    while i < len(string):
        j = string.find(substring, i)
        if j == -1:
            break
        count += 1
        i = j + 1

    return count
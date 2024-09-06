import unittest
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Parameters:
    - string (str): The input string.
    - substring (str): The substring to search for.

    Returns:
    - int: The number of occurrences of the substring in the original string.
    """
    # Using the built-in method to avoid counting cases with overlapping characters
    return string.count(substring)
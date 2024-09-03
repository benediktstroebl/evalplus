from typing import List
def longest(strings: List[str]):
    """ Outlines the function with type hints
    Returns the length of the longest string in the list
    """
    return max(strings, key=len)
strings = ["a", "bc", "c"]
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ 
    Filter an input list of strings and return only the ones containing the given substring.

    Args:
        strings (List[str]): The input list of strings.
        substring (str): Substring to filter by. Must not be empty.

    Returns:
        List[str]: Filtered list of strings.
    """
    if not substring:
        raise ValueError("Substring argument must not be empty")

    return [s for s in strings if substring in s]
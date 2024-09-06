from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # If the input list is empty, returning an empty string
    if not strings:
        return ''

    # Using join() to concatenate the strings in the list with a space separator
    return ' '.join(strings)
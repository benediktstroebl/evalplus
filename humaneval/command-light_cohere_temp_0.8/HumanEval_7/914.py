The Python script is:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring.

    Returns a specific list containing strings that contain the given substring.

    Parameters:
    strings: list of strings
    substring: string to filter for
    Returns: list of strings containing the given substring
    """
    return [string for string in strings if string. contains the substring]
```
This function creates a new list containing only the strings from the input list that contain the given substring.
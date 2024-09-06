Here's the self-contained Python function:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of strings
        substring (str): Substring to filter

    Returns:
        List[str]: List of strings containing the given substring
    """
    return [string for string in strings if substring in string]
```
This function takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The list comprehension with the filtering is done using the in operator, which checks if each string in the input list contains the given substring.
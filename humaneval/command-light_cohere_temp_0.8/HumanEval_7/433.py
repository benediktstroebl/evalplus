Here is a self-contained Python script that defines a function `filter_by_substring` solving the problem you have described:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of strings to filter
        substring (str): Substring to find

    Returns:
        List[str]: List of strings containing the substring
    """
    return [string for string in strings if substring in string.
```
This script defines a function that takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring.
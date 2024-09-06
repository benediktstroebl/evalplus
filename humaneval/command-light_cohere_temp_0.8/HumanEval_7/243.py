```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of strings to filter
        substring (str): Substring to search for

    Returns:
        List[str]: List of strings that contain the given substring
    """
    return [string for string in strings if string.contains(substring)]
```
Do you need help with anything else with Python or any other topic?
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of strings
        substring (str): Substring to filter

    Returns:
        List[str]: List of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```
Do you require additional assistance with code criterization, debugging, or other related topics?
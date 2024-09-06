```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    : Parameters:
        strings (List[str]) - List of strings
        substring (str) - The substring to search
    Returns:
        List[str] - List of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```
Do you require assistance with anything else? I can provide more code clarity or help with debugging this function.
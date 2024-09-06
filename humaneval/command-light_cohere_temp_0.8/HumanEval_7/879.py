```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain the given substring.
    Args:
    strings: list of strings
    substring: string to filter for
    Returns: list of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```
Do you require help with anything else?
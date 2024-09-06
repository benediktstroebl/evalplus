```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain the given substring.
    Args:
        strings: list of strings
        substring: substring to search in strings
    
    Returns: list of strings that contain the substring
    """
    return [s for s in strings if s.find(substring)]
```
Do you need help with anything else?
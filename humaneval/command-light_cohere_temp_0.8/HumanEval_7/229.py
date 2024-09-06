```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    :param strings: list of strings to filter
    :param substring: substring to search for
    :return: list of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```
Do you require assistance with anything else?
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain the given substring.

    :param
       
    list of strings: List of strings to filter
    :param substring: The substring to find
    :return: A list of strings that contain the substring
    """
    return [string for string in strings if string. contains substring]
```
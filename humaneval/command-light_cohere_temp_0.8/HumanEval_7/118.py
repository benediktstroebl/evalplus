```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring.

    :param
        strings: List of strings
    :param substring: The substring to filter for
    :return: List of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```
Do you need help with anything else related to Python programming?
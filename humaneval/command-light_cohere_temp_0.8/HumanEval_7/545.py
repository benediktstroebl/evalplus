```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain the given substring
    :param strings: list of strings
    :param substring: string to filter
    :return: list of strings containing the substring
    """
    return [string for string in strings if string. contains.strip(substring)]
 filters the strings in the list that contain the given substring, and returns a new list of those strings.
```
This function implements a simple filtering process to find and return a list of strings that include the specified substring.
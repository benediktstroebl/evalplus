```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring.
    :param strings: list of strings
    :param substring: string to filter for
    :return: list of strings that contain the given substring
    """
    return [s for s in strings if s.find(substring)]
```
Do you need any help with the code?
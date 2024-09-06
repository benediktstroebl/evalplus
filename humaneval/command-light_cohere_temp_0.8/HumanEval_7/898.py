```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    :param strings: list of strings
    :param substring: substring to filter
    :return: list of strings that contain the substring
    """
    return [x for x in strings if x.find(substring)]
```
Do you need help with anything else?
Here is a self-contained Python script that solves the problem you described: 
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring.

    if substring in a string:
            return [substring]
        elif substring in substring_list:
            return substring_list
        else:
            return []
    """

    # using if-elif to provide more specific return values
    # by checking multiple conditions with a single statement
    return [substring] if substring in strings else [substring] + filter_by_substring(strings, substring)
```
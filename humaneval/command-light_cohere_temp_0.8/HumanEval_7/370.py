```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    >>> filter_by_substring(['abc', 'bacd', 'cde'], 'd')
    []
    """
    return [s for s in strings if substring in s]
```
The filter_by_substring function in the code above takes a list of strings and a substring as input. It returns a
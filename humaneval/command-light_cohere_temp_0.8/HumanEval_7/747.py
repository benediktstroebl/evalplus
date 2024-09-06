Here is a Python script that includes a self-contained function that filters an input list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([ 'abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    >>> filter_by_substring([ 'abc', 'bacd', 'cde', 'array'], 'b')
    []
    """
    return [x for x in strings if substring in x]
```
The `filter_by_substring` function filters the list of strings based on whether the given substring is present in each string.
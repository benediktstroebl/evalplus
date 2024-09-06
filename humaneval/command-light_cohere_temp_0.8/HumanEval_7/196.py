Here is a self-contained Python script with a function that filters an input list of strings for those containing a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain the given substring.
    >>> filter_by_substring([ 'abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd']
    """
    return [x for x in strings if substring in x]
```
This function takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring. The test case demonstrates the only for the strings that contain the substring 'a', which are 'abc' and 'bacd'.
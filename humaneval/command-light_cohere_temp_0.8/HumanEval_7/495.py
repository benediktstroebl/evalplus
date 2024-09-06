Here is a Python script that defines a function `filter_by_substring` solving the problem you provided:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd']
    >>> filter_by_substring(['abc', 'bacdbac'], 'bac')
    ['abc', 'bacdbac']
    >>> filter_by_substring(['abc', 'abcde'], 'abc')
    ['abc', 'abcde']
    """
    return [x for x in strings if substring in x]
```

This function takes two parameters: `strings`, which is a list of strings, and `substring`, which is a string that we want to find within the strings in the list. It then returns a full list of strings from the input list that contain the given substring.

Note that the function is self-contained, and its purpose is to filter a list of strings based on the presence of a given substring within them.
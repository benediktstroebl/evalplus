Here is a self-contained Python script that implements the function `filter_by_substring` which filters an input list of strings based on whether the strings contain a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    >>> filter_by_substring(['abc', 'bd', 'cde'], 'd')
    ['cde']
    >>> filter_by_substring(['abc', 'def'], 'abc')
    ['abc']
    """
    return [string for string in strings if substring in string]
```

This code defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. It implements this problem by iterating through the list of strings and checking each string if the substring is present.

The code then provides several test cases to demonstrate the usage of the function, showing how it filters the strings correctly.
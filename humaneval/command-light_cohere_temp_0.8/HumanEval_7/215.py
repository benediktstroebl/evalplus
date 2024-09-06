Here is a Python script that includes the function `filter_by_substring` which solves the problem you described:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd']
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b')
    []
    """
    return [string for string in strings if substring in string]
```

This function takes two parameters: `strings`, which is a list of strings, and `substring`, which is a substring. It uses a duty list comprehension to iterate through the strings in the list and checks if each string contains the given substring using the `in` operator. The resulting list contains only the strings that passed the test.
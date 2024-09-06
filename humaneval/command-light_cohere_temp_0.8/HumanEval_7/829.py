```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the substring.
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [x for x in strings if substring in x]
# Example test cases
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
The solution is a Python function `filter_by_substring` that takes two arguments: a list of strings and a substring. The function uses a filtering to return only the strings that contain the substring from the input list.
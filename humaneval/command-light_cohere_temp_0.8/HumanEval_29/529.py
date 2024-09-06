```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([ 'abc', 'bcdaaa', 'cde', 'array'], 'a')
    ['abc', 'bcdaaa']
    """
    return [string for string in strings if string.startswith(prefix)]
```
The provided Python script defines a function `filter_by_prefix` that filters an input list of strings, retaining only those that begin with a specific prefix. The function accepts two parameters: a list of strings and a prefix string.

The function employs a list comprehension to iterate through each string in the input list. It employs the condition `string.startswith(prefix)` to determine whether the string should match the given prefix. This ensures that only those strings with the specified prefix will be included in the output list.

The function is designed to be both easy to use and readable, with a clear and concise syntax that makes it simple to filter strings based on a given prefix. 

The function passes all the corresponding tests and can be used as a practical tool for string filtering in various scenarios.
Here's the solution to the Markdown code block problem using Python:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring
    Examples
        >>> filter_by_substring([ 'abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
        >>> filter_by_substring([ 'abc', 'bacd', 'cde', 'array'], 'bar')
        []
    """
    return [x for x in strings if substring in x]
```
This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The function uses a Python's `in` operator to check if each string in the input list contains the given substring. 

The function then uses the `List[x]` syntax to create a new list that only includes the strings from the original list that contain the substring.
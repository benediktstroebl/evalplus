```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. This is achieved using a list comprehension, filtering out the elements that have a prefix that doesn't match the specified prefix.

Here's an example of how to use this function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'arr')
['array']
```

The output for both test cases is a list that contains only the strings from the input that begin with the specified prefix, thus demonstrating the functionality of the `filter_by_prefix` function.
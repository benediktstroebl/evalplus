```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that contains only the strings from the input list that start with the input prefix. The function uses a list comprehension to filter the strings. The output is an empty list if the input list is empty or if there are no strings that start with the given prefix.

Here is an example of an instance of the function being called:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This example illustrates the function correctly filtering out only the strings that start with the given prefix, 'a'.
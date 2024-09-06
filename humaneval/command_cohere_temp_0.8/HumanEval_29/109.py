```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that have the specified `prefix`. The behaviour is defined by the `startswith` method, which returns `True` if the beginning of the string matches the `prefix` argument.

Here's how the function works when invoked with different inputs:
```python
filter_by_prefix([], 'a')  # Returns: []
filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')  # Returns: ['abc', 'array']
``` 

In the first example, the empty list remains empty after passing it through the function. In the second example, the list is filtered, and only the strings with the prefix 'a' are returned.
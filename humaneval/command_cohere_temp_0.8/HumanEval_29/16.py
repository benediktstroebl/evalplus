```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. This is accomplished via a list comprehension, using a generator expression as the filter condition, `s.startswith(prefix)`, to test if a string, `s`, starts with the specified `prefix`. The `List[str]` return type is inferred from the type of the input `strings` parameter, and the function is annotated with a type hint for the same.

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

This would return a list containing only two strings: 'abc' and 'array', as these are the only inputs that start with the 'a' prefix.
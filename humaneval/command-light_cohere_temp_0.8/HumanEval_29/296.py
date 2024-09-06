Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'a'

# Result
print(filter_by_prefix(strings, prefix))  # ['abc', 'array']
```
The code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with that given prefix. The function uses the use list comprehension to filter the input list and return only the strings that start with the given prefix.
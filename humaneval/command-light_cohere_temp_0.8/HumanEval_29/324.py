```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "xx", "zz"]
prefix = "a"

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```
The function filter_by_prefix takes a list of strings and a prefix as inputs and returns a new list of strings that start with the specified prefix. This function efficiently uses the In Python, list comprehensions are typically used to filter elements of lists, and the function leverages Python's typing and list comprehension to implement this task.
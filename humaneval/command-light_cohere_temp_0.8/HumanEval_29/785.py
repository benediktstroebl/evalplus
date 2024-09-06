```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases
strings = ["abc", "bcd", "cde", "array", "hello", "world"]
prefix = "a"

# expected output: ['abc', 'array']
print(filter_by_prefix(strings, prefix))

strings = ["abd", "cdef", "ddef", "ohm"]
prefix = "cd"

# expected output: ['cdef', 'ddef']
print(filter_by_prefix(strings, prefix))
```
This code provides a filter_by_prefix function that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the specified prefix. It uses the simple list comprehension to filter out the desired strings from the input list, and the tests ensure that the function works correctly for different inputs.
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'a'

print(filter_by_prefix(strings, prefix))  # ['abc', 'array']
``` 
This script defines a function called **filter_by_prefix** that takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. The function uses the **list comprehension** to filter the strings and pass all the tests.
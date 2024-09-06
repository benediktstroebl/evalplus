```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "start"]
prefix = "a"

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
``` 
This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. The function then uses the string starting with the given prefix to filter the input list.
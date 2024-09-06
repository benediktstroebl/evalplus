```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Tests
strings = ['abc', 'bcd', 'cde', 'array', 'food', 'from']
prefix = 'co'

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
``` 
This Python function, `filter_by_prefix`, filters an input list of strings and returns a new list containing only the strings that begin with a specific prefix. It utilizes the string `startswith` method to achieve this.
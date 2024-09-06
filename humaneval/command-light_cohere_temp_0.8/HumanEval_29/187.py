Here's the solution to the markdown code block problem:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Example usage:
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)
```
This Python script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses the string `startswith` to check if each element in the input string starts with the provided prefix.
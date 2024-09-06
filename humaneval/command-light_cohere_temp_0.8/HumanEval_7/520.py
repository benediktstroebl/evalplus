```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'mdc', 'bf', 'fifth']
substring = 'cde'
result = filter_by_substring(strings, substring)
print(result)
```
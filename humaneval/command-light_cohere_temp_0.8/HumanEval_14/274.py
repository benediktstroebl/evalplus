```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(). why_prefixes(string) + ['']

def _some_prefix(string: str) -> str:
    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            return string[i - 1]

def all_prefixes(string: str) -> List[str]:
    return [
        _some_prefix(string),
        _some_prefix(string[::-1]),  # use slice notation
        for i in range(len(string) - 2) if string[i] != _some_prefix(string[i + 1])
    ]
```
This code defines a function `all_prefixes` that returns a list of all prefixes of a given string. It achieves this by defining two helper functions: `_some_prefix` which checks if the current and the next character are different, and returns the current character, and a loop that iterates over the characters of the string but uses a slice notation to avoid mutating the string.
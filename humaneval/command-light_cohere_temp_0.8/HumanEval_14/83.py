```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.a.join([char(string) for string in string.split('')] if prefix != '')]
```

This Python function, all_prefixes, creates a list of all prefixes from shortest to longest in a given input string. It uses list comprehension and the `split()` function to create an array of substrings from the input string. The `join` method iterates over the array of substrings and checks if the prefix is not an empty string using the `if` condition. This effectively captures all prefixes.
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This is a common operation when you need to filter a list of items based on a certain condition and want to reuse the logic across different parts of the codebase. The function utilizes list comprehension, making it more readable and concise.

Given the arguments `[]` and `'a'`, the expected output would be `[]`. Conversely, given the arguments `['abc', 'bcd', 'cde', 'array']` and `'a'`, the expected output would be `['abc', 'array']`.
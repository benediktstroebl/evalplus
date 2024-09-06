```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Testing the function with various inputs
strings = ['abc', 'bcd', 'cde', 'array', 'welcome', '123']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```

The above Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses the specific input types and returns a new list containing elements that start with the specified prefix. The test case shows that the function works correctly for the given inputs.
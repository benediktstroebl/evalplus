```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix."""
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output ['abc', 'array']

# Test case 2: invalid prefix
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'x'
result = filter_by_prefix(strings, prefix)
print(result)  # Output []
```
This code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It takes a example of using this function to filter strings starting with 'a' and prints the result, which is ['abc', 'array']. The function also has test cases to ensure the function works correctly for different inputs.
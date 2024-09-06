```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests for filter_by_prefix function
def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['a', 'bb', 'ccc'], 'bb') == []
```
This Python code defines a function `filter_by_prefix` that filters an input list of strings based on their prefix. The function takes two parameters: a list of strings `strings` and a prefix `prefix` as input. The function creates a filter using list comprehension and returns a new list containing only the strings from the input list that start with the specified prefix.

The code also includes unit tests for the `filter_by_prefix` function using the `assert` function to verify its correctness. This ensures the can be used to test and validate your custom function.
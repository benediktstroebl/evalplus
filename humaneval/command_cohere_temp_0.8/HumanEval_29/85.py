```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that start with the `prefix`. It uses a list comprehension, which is a concise way of expressing a map and a filter operation at the same time. On each iteration, it applies the condition `string.startswith(prefix)` to filter elements of the `strings` list and then collects those that pass the test into the `return_list`. 

The function includes type hints for the argument and return types, using the `typing` module. This helps provide better documentation and enables features like static type checking. Although not included in this code block, it's best to include tests to ensure the function works correctly across different scenarios. Tests could be added in the code block like so:
```python
# Test cases for the filter_by_prefix function
assert filter_by_prefix([], 'a') == []
assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar') == ['array']
assert filter_by_prefix(['one', 'two', 'three', 'four'], 't') == ['two', 'three']
```
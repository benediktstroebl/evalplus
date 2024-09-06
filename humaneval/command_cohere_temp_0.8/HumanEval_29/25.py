```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. It uses a list comprehension to iterate over each string in the input `strings`, and checks if it starts with the specified `prefix`, using the `startswith` method. If a string starts with the prefix, it's included in the resulting list. If it doesn't, it's excluded. 

This solution adheres to the type hinting technique by providing an explicit type annotation for the function's return value, which improves code readability and ensures compatibility with static type checkers, allowing for robust and error-free programming. 

You can verify the correctness of the function by calling it with different test cases. Here's an example:
```python
# Test case with an empty list and a prefix
result = filter_by_prefix([], 'a')
print(result)  # Output: []

# Test case with a list of strings and a matching prefix
result = filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
print(result)  # Output: ['abc', 'array']

# Test case with a list of strings and an non-matching prefix
result = filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z')
print(result)  # Output: []
```

These examples demonstrate the functionality of the `filter_by_prefix` function and its ability to filter strings based on their prefixes, as specified in the problem statement.
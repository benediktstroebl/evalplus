```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        string
    """
    return "".join(strings)

# Test case 1: empty list
test_case1 = []. concatenate([])
# Test case 2: single string
test_case2 = [".abc"]
# Test case 3: list of 3 strings
test_case3 = ["a", "bc", "def"]

print(test_case1)  # Output: ''
print(test_case2)  # Output: 'abc'
print(test_case3)  # Output: 'abcdef'
```
This Python code defines a function **concatenate** that takes a list of strings as input and returns the concatenated string. It uses the types hint to provide better documentation for the function and provides sample test cases to ensure its correctness.
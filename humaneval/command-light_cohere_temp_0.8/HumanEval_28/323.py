```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(''.join(strings, join=''))

# Example test cases
test_cases = [
    [],
    ['a'],
    ['a', 'b', 'c'],
    ['a', 'b', 'ccc'],
]

# Function test
for case in test_cases:
    assert concatenate(case) == ''.join(case, join='')
```
The provided code defines a function `concat` that concatenates a list of strings into a single string. It uses the string interpolation with the `join` method to combine the strings into a single string. The code also includes a list of test cases, and for each test case, it asserts if the result of the `concat` function matches the expected output. 

This code provides a self-contained way to solve the problem of concatenating strings in Markdown format.
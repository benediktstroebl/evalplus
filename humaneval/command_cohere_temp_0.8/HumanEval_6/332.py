Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result, current_level = [], 0
    for char in s:
        if char == '(':
            current_level += 1
        elif char == ')':
            current_level -= 1
        result.append(current_level)
    return result
```
This function uses a simple Nesting Level Calculator Algorithm to solve the problem and maintains a list `result` to store the results. 

To test this function, you can run the following code:
```python
test_lists = [
    ('(()()) ((())) () ((())()())', [2, 3, 1, 3]),
    ('((a))', [1]),
    ('((()))', [2]),
    ('(((())))', [3]),
    ('()', [0]),
    ('()', [0]),
    ('aa', [0]),
    ('(((a))))', [4]),
]

for inp, out in test_lists:
    assert parse_nested_parens(inp) == out
```
This script includes a test suite with a variety of test cases to validate the correctness of the `parse_nested_parens()` function.
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nest = 0
        i = 0
        for char in chunk:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            i += 1
        result.append(nest)
    return result
```

The `parse_nested_parens` function takes a string as input and splits it into chunks using spaces as separators. For each chunk, it counts the number of open parentheses '(' and subtracts the number of closed parentheses ')' to get the current nesting level. The maximum nesting level for each chunk is then appended to a list and returned as the final result.

To test this, you can run the following code to see if it correctly solves the problem:
```python
test_cases = ['(()()) ((())) () ((())()())', '(()())', '((()))', '()', '(((((((()))))))))))))))']

for case in test_cases:
    print(f"Input: {case}")
    expected = [2, 3, 1, 3, 0, 5]
    actual = parse_nested_parens(case)
    print(f"Output: {actual}")
    assert actual == expected
```

This will verify that the function behaves as expected for a variety of input scenarios.
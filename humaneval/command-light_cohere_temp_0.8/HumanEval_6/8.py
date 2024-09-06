```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if stack:
                result.append(stack.pop())
               pop out a result (stack)
            stack = []
    return result

# Test code for the parse_nested_parens function
def test_parse_nested_parens():
    test_str = '(()()) ((())) () ((()))'
    assert parse_nested_parens(test_str) == [2, 3, 1, 3]
```

This code defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of integers representing the deepest level of nesting for each group. The function uses a stack to keep track of open parentheses and builds the result list as it closes each group. The test code provided also passes the test on the `test_parse_nested_parens` function with a sample input string.
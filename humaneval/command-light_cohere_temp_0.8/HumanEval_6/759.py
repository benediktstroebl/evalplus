```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    levels = 0
    out = []
    for char in parentheses_string:
        if char == '(':
            stack.append(levels)
        levels += 1
        elif char == ')':
            if levels == 0:
                raise ValueError("Unexpected character ')'!")
            stack.pop()
            if levels > 0:
                out.append(levels)
                levels -= 1
        else:
            stack.append(levels)
    levels += 1
    return out

# Tests
def test_parse_nested_parens():
    test_cases = [
        "(()()) ((())) () ((())())",",
        "((()))",
        "((())) ()",
        "()()()()()"
    ]
    for test_case in test_cases:
        actual_result = parse_nested_parens(test_case)
        expected_result = [2, 3, 1, 3]
        assert actual_result == expected_result, f"Test case [{test_case}] failed."
# Run the tests
test_parse_nested_parens()
```
This code defines a function `parse_nested_parens` that parses and returns the deepest level of nesting of parentheses in a given string. The function uses a stack to keep track of the nesting levels and the out list to store the deepest level of nesting of parentheses. The tests section contains a test cases with various formats of input strings, and the `test_parse_nested_parens` function verifies that the output of the `parse_nested_parens` function matches the expected output for each test case. 
The code is well-contained, and the function and tests can be executed independently.
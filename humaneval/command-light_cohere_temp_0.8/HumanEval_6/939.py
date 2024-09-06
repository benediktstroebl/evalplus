```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack: List[int] = []
    left, right = 0, 0
    for i, char in enumerate(parenthes_string):
        if char == '(':
            left = i
        elif char == ')':
            right = i
        else:
            if left > 0 and right < len(parenthes_string) - 1:
                stack.append(parentheses_string[left:right])
                left = right + 1
                right = i
    return stack
def test_parse_nested_parens():
    test_str = '(()()) ((())) () ((())()())'
    result = parse_nested_parens(test_str)
    assert result == [2, 3, 1, 3]
test_parse_nested_parens()
 ```
This code defines the `parse_nested_parens` function that takes a string of parentheses as input and returns a list of their depths. The `test_parse_nested_parens` function tests the `parse_nested_parens` function with a sample string and verifies that the output is correct.
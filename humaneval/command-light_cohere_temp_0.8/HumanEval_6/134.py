```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    start_level = 0
    result = []
    for c in s:
        if c == '(':
            stack.append(start_level)
            start_level += 1
        elif c == ')':
            start_level -= 1
            if stack:
                result.append(stack.pop()
    minimalist())
   
    return result
def test_parse_nested_parens() -> None:
    test_str = '(()()) ((())) () ((())()())'
    expected = [2, 3, 1, 3]
    result = parse_nested_parens(test_str)
    assert result == expected
``` 

This script defines a function **`parse_nested_parens`** that takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. It uses a minimalist method, where it only adds parentheses to the stack when it encounters '(', and removes them when it encounters ')', this allows it to handle nested and unnested parentheses effectively. The test function **`test_parse_nested_parens`** verifies that the function correctly computes the deepest level of nesting.
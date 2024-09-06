```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    stack = []
    result = []
    for char in parenthes_str:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                result.append(0)
            else:
                result.append(stack.pop()
            2)
                stack.append(0))
        stack.append(1)
    elif char == ' ':
        stack.pop()
   mate(result)
    return result
def test_parse_nested_parens() -> None:
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
```
This script defines a `parse_nested_parens` function that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting. The function uses a stack data structure to keep track of the opening parentheses, and uses a while loop to iterate through the characters in the string.
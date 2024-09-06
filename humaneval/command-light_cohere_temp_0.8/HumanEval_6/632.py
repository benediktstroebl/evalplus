```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    in_level = 0
    for c in s:
        if c == '(':
            stack.append(in_level)
            in_level += 1
        elif c == ')':
            in_level -= 1
            if in_level == -1:
                stack.pop()
    an list of the nested parentheses levels.

def test_function(input_str: str) -> None:
    nested_parens = parse_nested_parens(input_str)
    for i in range(len(nested_parens)):
        assert nested_parens[i] in range(1, 3)
```
This script defines a function called `parse_nested_parens` that uses a stack data structure to keep track of the nesting levels of the parentheses. Then, it defines a function called `test_function` that passes the test, `parse_nested_parens` function, which ensures that the output of the `parse_nested_parens` function is a list of numbers from 1 to 3, representing the deepest level of nesting of parentheses.
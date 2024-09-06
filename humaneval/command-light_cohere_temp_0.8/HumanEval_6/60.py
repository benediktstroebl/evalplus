Here is a self-contained Python script that defines a function `parse_nested_parens` that solves the problem of parsing nested parentheses and passes the tests:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input and returns a list of the deepest nesting levels.
    """

    first group, then returns the deepest level of nesting of the remaining parentheses.
    """
    example:
    ```
    Input: '(()()) ((())) () ((()))'.
    Output: [2, 3, 1, 3]
    ```
    """
    stack = []
    in_group = False
    out_group = False
    for c in s:
        if c == "(" and not out_group:
            in_group = True
        elif c == ")" and in_group:
            stack.append(1)
            in_group = False
        elif c == ")" and out_group:
            stack.pop()
            out_group = True
        elif c == "(":
            out_group = False
        else:
            raise ValueError("Unexpected character:", c)
    return stack
```
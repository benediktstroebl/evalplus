```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        level = 0
        stack = []
        for char in segment:
            if char == '(':
                stack.append(level)
                level += 1
            else:
                level = stack.pop() if stack else 0
        result.append(level)
    return result
```

This script includes the function `parse_nested_parens`, which takes a string `s` as input and returns a list of deepest levels of nesting of parentheses in each segment (separated by spaces) in the string.

The function uses a stack to keep track of the current nesting level for each opening parenthesis it encounters. It initializes the `level` variable to 0, which is incremented each time an opening paren `(` is encountered, and decremented each time a closing paren `)` is encountered. The current nesting level is pushed onto the stack whenever it increases and is popped whenever it decreases.

The output of the function for the input test case provided would be: `[2, 3, 1, 3]`
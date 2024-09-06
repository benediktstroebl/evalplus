```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        stack = []
        depth = 0
        for char in chunk:
            if char == '(':
                stack.append(depth)
                depth += 1
            else:
                depth = stack.pop()
        if stack:
            result.append(stack.pop())
        else:
            result.append(depth)
    return result
```

The `parse_nested_parens` function takes a string as input and returns a list of the deepest nesting level of parentheses in each sub-string. It splits the input string into chunks by spaces, and iterates through each character of each chunk, maintaining a stack of depths of parentheses encountered so far. When the closing parentheses exceeds the opening parentheses, the top of the stack contains the deepest nesting level of that specific stretch of parentheses, otherwise, the number of closing parentheses denotes the depth. The final result is a list of these deepest nesting levels for each sub-string.
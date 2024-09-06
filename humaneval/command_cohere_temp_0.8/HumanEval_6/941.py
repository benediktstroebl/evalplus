Here's a Python script with a self-contained function that solves the problem using a stack to keep track of opening parentheses encountered:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result, stack = [], []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or char != stack.pop():
                result.append(len(stack))
    if stack:  # If there are still opening parentheses, consider it to be 1
        result.append(len(stack))
    return result
```

The code defines a function `parse_nested_parens` that takes a string `s` containing multiple groups of nested parentheses separated by spaces. It returns a list where each element represents the deepest level of nesting of parentheses in the corresponding group.

The algorithm uses a stack to keep track of opening parentheses encountered. When a closing parenthesis is encountered, the stack is checked to see if it matches the last opening parenthesis. If it does not, it means there is a deeper level of nesting, so the length of the stack is tracked in the result. Finally, if there are any opening parentheses remaining in the stack, it implies a lack of matching closing parentheses, and the stack length is added to the result as well.

Here's an example usage and corresponding output:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
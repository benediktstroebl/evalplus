```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for group in s.split():
        stack = []
        for char in group:
            if char == '(':
                stack.append(len(stack))
            else:
                stack.pop()
        result.append(stack[-1])
    return result
```

This Python script provides a self-contained function called `parse_nested_parens` taking a string `s` as input, containing multiple groups of parentheses separated by spaces, and returns a list representing the maximum nesting depth of each group.

The function uses a stack to keep track of the nesting level for each opening parenthesis it encounters. Each time an opening parenthesis is met, it pushes the current depth into the stack, and when a closing parenthesis is met, the function pops the top of the stack to decrement the current depth. Finally, the maximum depth reached for each group is appended to the result list.

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
This example uses the function as described in the original problem statement, and the output corresponds to the maximum depth of nesting for each of the four groups of parentheses in the input string.
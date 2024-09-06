```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    l = 0
    while l < len(s):
        char = s[l]
        if char == "(":
            stack.append(1)
        elif char == ")":
            if not stack or stack[-1] != 1:
                stack.append(0)
            else:
                stack.append(stack.append(1))
        else:
                stack.append(0)
        l += 1
    return stack
```
Now, the `parse_nested_parens` function takes a string as an argument and returns a list of integers representing the deepest level of nesting of parentheses in the string. It uses a stack data structure to track the open parentheses in the string. The function goes through the open parentheses one by one and uses the stack to keep track of the open parentheses.
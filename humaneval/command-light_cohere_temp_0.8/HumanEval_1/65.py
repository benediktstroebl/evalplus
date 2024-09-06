Here's the solution:

```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses from the input string.
    >>> separate_paren_groups('( )((()))')
    ['(', ')()', '(()())']
    """
    result = []
    stack = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] == ')':
                result.append(''.append(char)
                stack = []
            else:
                stack.pop()

   
   [-1] = ')'
                result.append(')'.
return result
```

This function uses a stack to keep track of open parentheses, it starts with the first '(' character, when it encounters the corresponding ')' it pops it from the stack, closing the current group, and appends the new character. 
The function will return a list of separate balanced parentheses.
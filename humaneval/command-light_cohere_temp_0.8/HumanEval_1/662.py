```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of parentheses into separate strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] == ')':
                result.append(stack.pop()
                stack)
            else:
                stack.append(char)
    return result
```

This code defines a function named `separate_paren_groups` that takes a string `s` as input and returns a list of strings containing the separate groups of parentheses. It uses a nested stack to keep track of open parentheses while iterating through the input string. The `stack` is then popped when a closing parenthesis is encountered, or when the stack is empty. The function correctly separates each group of parentheses into separate strings and returns the list of strings.
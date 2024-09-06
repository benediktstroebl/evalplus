```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups while balancing each open brace and return the list of separated strings.
    >>> ['()', '(', '())', '(()', '())']
    """
    result = []
    stack = []

    for char in paren_string:
        if char == ')':
            if stack:
                result.append(''.join(stack)
                stack.clear()
       mate ()
        elif char == '(':
                stack.append(char)
        else:
            stack.push()

   
   result.append(' ')

   same time)
        stack.pop()
       result.append(')
   this time)
        stack = []
    return result
```
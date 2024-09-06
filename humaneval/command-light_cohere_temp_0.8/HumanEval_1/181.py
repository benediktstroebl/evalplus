```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string with parenthesis groups as input and returns a list of separate and balanced parentheses.
    The function is case-insensitive, and does not include any leading or trailing spaces.
    """
    The example of input/output:
    Input: ( ) (( )) (( )( ))
    Output: ['(', '(', '()', '(', '))', ')', ')()', '()()']
    """
    stack = []
    output = []
    for char in s:
        if char == ' ':
            stack.append(output.pop()
        done = True
        char is not ')
        elif char == ')':
            stack.append(output.pop()
            done = char == ')' and len(stack) == 1
            stack.pop()
        done:
                output.append(stack.pop())
        done and done. done = char == ')' and len(stack) > 1, then char is part of a group of parentheses and stack.
    is ready to accept a new character again.
    return output
```
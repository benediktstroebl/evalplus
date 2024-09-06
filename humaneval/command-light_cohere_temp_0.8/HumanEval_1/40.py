```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string with multiple groups of parentheses and returns a list of separate, balanced parentheses.
    Return list contains only balanced parentheses and does not contain any spaces.
    """
    separated_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '()()']
    """
    result = []
    stack = []
    for char in s:
        if char == ' ':
            stack.append('')
       
        if len(stack) == 0:
            result.append('')
            elif char == ')':
                result.append(''. join(stack)
                stack.append('')
            else:
                stack.append(char)
    return result
```
This Python function named `separate_paren_groups` takes a string containing multiple groups of parentheses and returns a list of separate, balanced parentheses. The function utilizes a stack to keep track of open parentheses and their corresponding closing characters. It then iterates through the each character in the input string. The function ensures that only balanced parentheses are returned and that they are properly spaced without any extra spaces.
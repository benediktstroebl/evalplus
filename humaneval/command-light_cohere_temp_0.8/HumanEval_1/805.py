```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Purpose: This function takes a string of parenthesis-enclosed groups as input and returns a list of separate and balanced parentheses, without any nested.

    Input: The string of parenthesis-enclosed groups may contain multiple types of parentheses and spaces.
    Output: Returns a list of separated and balanced parentheses.
    """
    example usage:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    list_output = []
    stack = []

    for char in s:
        if char == ' ':
            stack.append(char)
        if len(stack) == 1:
            list_output.append(''.append(stack.pop())
       
            list_output.append(char)
        stack = []
    return list_output
```
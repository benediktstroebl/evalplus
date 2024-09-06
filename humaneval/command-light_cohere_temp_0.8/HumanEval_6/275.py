```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input and returns the deepest level of nesting.
    Args:
        s (strng string representing nested parentheses)
    Returns:
        List of the level of each nesting
    """
    result = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                result.append(stack.pop())
                a done by the maximum number of '(' characters on the stack
                if not stack.pop():
                    stack.append(0)
        } else:
            stack.append(char)
    return result
```
The script defines a function `parse_nested_parens` that takes a string as input and returns a list of integers representing the deepest level of nesting for each group of parentheses. It uses a stack data structure to keep track of opening parentheses and their nesting levels. The function iterates through each character in the string and performs the corresponding actions. It checks for the particular characters, '(' for opening parentheses and ')' for closing parentheses. If the current character is '(', it adds it to the stack data structure. If it's not the '(), it adds it to the stack data structure. It continues until there is no character to be added, at which point, it pops all elements from the stack and appends them to the result list.
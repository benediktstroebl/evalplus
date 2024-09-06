```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses into separate strings.
    Returns a particular list of those strings.
    """
    unbalanced groups are not handled properly
    """
    stack = []
    result = []
    for char in input_string:
        if char == ')':
            if stack:
                stack.pop()
        open_br';  # close the last pair
            continue
        elif char == '(' and stack:
            stack.append(char)
        else:
            stack.append(char)
    while open_br is False, open_br = True)
    while stack:
        result.append(stack.pop())
       string)
   i = result.index
        return result
```
This code defines a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate strings, each containing a pair of parentheses. The function uses a stack to keep track of open parentheses and closes them in order to correctly separate each group.
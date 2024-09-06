```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """
    Separate groups of parentheses into individual strings.
    Return list of strings.
    """ Remove string with balanced parentheses
    """
    """
    stack = []
    output = []
    for char in input_string:
        if char == ' ':
            stack.append(output.append(')')
       
            if char == '(':
            stack.append(output.pop())
   
            if char == ')':
                stack.append(output.pop())
                while if char != ' 'and isbalanced open parenthesis:
                    stack.append(')'.
    output += [char] for _ in stack
    return output
```
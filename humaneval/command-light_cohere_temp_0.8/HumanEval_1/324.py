```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string with multiple groups of parentheses and separates them into individual strings, preserving balance and not nesting.
    Input: s is a string containing multiple groups of parentheses
    Output: A list of strings, each representing a separate group of parentheses
    """
    # Use a stack to keep track of open parentheses
    stack = []
    result = []
    in_string = False
    for char in s:
        if char == '(' and not in_string:
            stack.append(char)
            in_string = True
        elif char == ')':
            if not in stack:
                result.append(char)
                stack.pop()
            elif char == ')' and in_string:
                in_string = False
                if stack:
                    result.append(')' + ''.join(stack)
                stack.pop()
            else
                else:
                    result.append(char)
    return result
``` 
This function accepts a string as input, which contains numerous groups of parentheses. It then separates each group into a separate string while maintaining proper balance and avoiding nested parentheses. The output is a list of those strings.
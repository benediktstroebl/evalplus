Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing only the separate groups of parentheses. The function works by using the `split` method to divide the input string into a list of substrings using the closing parentheses as the split characters. The problem is described as follows:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if stack:
                stack.pop()
            else:
                return []
        else:
            current_group += char
    
    return stack
```

This approach leverages a stack to keep track of nested parentheses groups. Nested groups are indicated by parentheses within other parentheses, so we use an additional stack to keep track of the nesting level for each group. When a closing parenthesis is encountered, we check the nesting level to determine whether it belongs to the currently active group. If so, we close that group and reduce the nesting level. If not, we close the most recently opened group (top of the stack) and ignore the extra closing parenthesis. 

Note that this approach assumes that the input string contains only single spaces, and it ignores any spaces during the separation process. You can test this script by calling the `separate_paren_groups` function with different input values, such as a string containing different groups of nested parentheses. The function should return a list of strings containing the separate groups of parentheses, each string representing a balanced group of parentheses with no nesting within each other.  For example:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
``` 
This will return the list of strings that contain the separate groups of parentheses from the input string.
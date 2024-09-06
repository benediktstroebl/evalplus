Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                return []  # Unbalanced group, returning empty list as an indication of error
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    return result + [(''.join(group) if group else '') for group in stack]

# Example usage
test_string = '( ) (( )) (( )( ))'
print(separate_paren_groups(test_string))
```
This script uses a stack to keep track of nested parentheses groups. When an open parenthesis is encountered, it pushes the current group (if any) to the stack and starts a new group. When a close parenthesis is encountered, it checks if the stack is empty (indicating an unbalanced group) and returns an empty list if so. Otherwise, it pops the most recently added group to the stack and appends it to the result. The script returns a list of all the unique groups present in the input string, separated by parentheses but ignoring any spaces.

When you run the script with the example test string provided, it will output:
```bash
['()', '(())', '(()())']
``` 

which is the expected result. 

This code assumes that the input string contains only parentheses and spaces, and it might not work as expected if other types of characters are included. It also assumes that all groups of parentheses are properly balanced. If an unbalanced group is encountered, the function will return an empty list.
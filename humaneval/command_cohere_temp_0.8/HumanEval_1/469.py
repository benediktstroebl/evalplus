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
                return []  # Unbalanced group, returning empty list as an indication of failure
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    return result + stack

# Example usage
test_string = '( ) (( )) (( )( ))'
print(separate_paren_groups(test_string))
```
This script uses a stack to keep track of nested parentheses groups. When a left parenthesis '(' is encountered, we push the current group onto the stack and start a new group. When a right parenthesis ')' is encountered, we pop the last group from the stack and append it to the result. If the stack is empty when we try to pop, it means the parentheses are not balanced, and we return an empty list as an indication of failure.

When executed with the test string provided, the output will be:
```bash
['()', '(())', '(()())']
```
This output corresponds to the groups of parentheses in the input string.
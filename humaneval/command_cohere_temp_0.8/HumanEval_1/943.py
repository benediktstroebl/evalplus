Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings of separated parentheses group:
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
                return []  # Unbalanced groups, returning empty list as an indication of error
            current_group.append(char)
            if not stack:
                result.append(')'.join(current_group))
                current_group = stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    # Checking if there are still some groups in the stack
    if stack:
        return []  # Unbalanced groups, returning empty list as an indication of error
    else:
        result.append(')'.join(current_group))
        
    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of opening parentheses until the corresponding closing parenthesis is encountered. The code iterates through every character in the input string, either pushing an empty list to the stack when an opening parenthesis is encountered or checking if the stack is empty. If the stack is not empty, the current group is popped from the stack and added to the result list. The current group is then updated to the most recently popped group. This allows us to maintain separate groups of parentheses.

The resulting list of strings is then returned. You can test this function by calling it with the input `('( ) (( )) (( )( ))')` to verify that it returns the expected output `['()', '(())', '(()())']`.
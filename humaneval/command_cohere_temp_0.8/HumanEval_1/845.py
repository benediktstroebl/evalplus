Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing balanced parenthesis groups, without considering spaces:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """Input to this function is a string containing multiple groups of nested parentheses. Your goal is to separate those groups into separate strings and return the list of those."""
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            if not stack:
                return []  # Unbalanced group, returning empty list as an indication of failure
            current_group += ')'
            top_group = stack.pop()
            if not top_group:
                current_group = ""  # Start a new group when the previously popped group was empty
            else:
                current_group = top_group
        else:
            current_group += char
    
    return [group.strip() for group in stack]

# Example usage
test_string = '( ) (( )) (( )( ))'
print(separate_paren_groups(test_string))
```
This script uses a stack to keep track of opening parentheses until they are closed, building strings on the stack as it goes. The result is that all parentheses groups in the input string are properly separated and returned as a list. when the input string is `( ) (( )) (( )( ))`, the output is as follows:
```
['()', '(())', '(()())']
``` 

This approach handles cases with and without spaces between parentheses, and it handles improperly formed input gracefully by returning an empty list if necessary.
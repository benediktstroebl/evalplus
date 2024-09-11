### Separate Paren Groups

Here is a Python script that solves the problem using a stack data structure to keep track of the opening parentheses:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.

    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize a stack and a list to store the groups
    stack = []
    groups = []

    # Iterate over the parentheses string
    for paren in paren_string:
        # If the parenthesis is an opening parenthesis, push it to the stack
        if paren == '(':
            stack.append(paren)
        # If the parenthesis is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif paren == ')':
            group = ''
            while stack and stack[-1] == '(':
                group = stack.pop() + group
            # If the stack is empty after popping, add the current group to the list of groups
            if not stack:
                groups.append(group)

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script defines a function `separate_paren_groups` that takes a string of parentheses as input. It removes any spaces from the string, initializes a stack to keep track of the opening parentheses, and a list to store the groups. It then iterates over the string, pushing opening parentheses to the stack and popping corresponding closing parentheses. When a closing parenthesis is encountered without a corresponding opening parenthesis, the current group is added to the list of groups. The function returns the list of groups.

The script also includes a test case to verify the correctness of the function.
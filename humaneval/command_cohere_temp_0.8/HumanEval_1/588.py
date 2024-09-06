Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing balanced parenthesis groups, without considering spaces:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                return []  # Unbalanced group, returning empty list as an indication of failure
            current_group.append(char)
            if not stack:
                return []  # Unbalanced group, returning empty list as an indication of failure
            stack.pop()
        else:
            current_group.append(char)

    # Handle potential unbalanced groups
    if stack:
        return []  # Unbalanced groups, returning empty list as an indication of failure

    return current_group

# Example usage
print(separate_paren_groups("( ) (( )) (( )( ))"))
```
The script works as follows:
1. It uses a stack to keep track of opening parentheses `(` and a list `current_group` to keep track of the currently balanced parentheses group.
2. Whenever an opening parenthesis `(` is encountered, it pushes the current group onto the stack and starts a new group.
3. Whenever a closing parenthesis `)` is encountered:
   - If the stack is empty, this is an unbalanced group, and we return an empty list as an indication of failure.
   - If the stack is not empty, we pop the stack to close the correct opening parenthesis, add the closing parenthesis to the current group, and proceed.
4. Other characters (non-parentheses) are simply added to the current group.
5. After processing all characters, it checks if there are any opening parentheses left in the stack. If so, it returns an empty list as an indication of failure, since there are unbalanced groups.
6. If there are no unbalanced groups, it returns the list of strings corresponding to the balanced groups.

The example usage at the end demonstrates its behavior on a sample input.
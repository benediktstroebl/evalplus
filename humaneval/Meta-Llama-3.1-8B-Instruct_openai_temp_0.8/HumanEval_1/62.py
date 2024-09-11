```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate balanced groups of nested parentheses from a given string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate groups of balanced parentheses.
    """
    stack = []
    groups = []
    start = 0
    for end, char in enumerate(paren_string):
        # push opening parenthesis to the stack
        if char == '(':
            stack.append(char)
        # pop the last opened parenthesis from the stack
        elif char == ')':
            if stack:
                stack.pop()
                # if the stack is empty after popping, it means we have found a complete group
                if not stack:
                    # add the complete group to the groups list and update the start index
                    groups.append(paren_string[start:end+1])
                    start = end + 1
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the opening parentheses encountered so far. When a closing parenthesis is encountered, the script pops the last opening parenthesis from the stack. If the stack becomes empty after popping, it means we have found a complete group, which is then added to the list of groups. The script also keeps track of the start index of each group to correctly extract the complete groups from the input string.
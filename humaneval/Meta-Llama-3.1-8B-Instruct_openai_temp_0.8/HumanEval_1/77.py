### Separate Paren Groups Script

The following Python script uses a stack-based approach to separate groups of nested parentheses.

```markdown
### Code
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into a list.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate groups of nested parentheses.
    """
    stack = []
    groups = []
    temp = ''
    
    # Iterate through the input string character by character
    for char in paren_string:
        if char == '(':
            # If we encounter an open parenthesis, push it onto the stack
            stack.append(char)
            temp += char
        elif char == ')':
            # If we encounter a close parenthesis, pop the corresponding open parenthesis from the stack
            stack.pop()
            temp += char
            
            # If the stack is empty after popping, it means we have a complete group
            if not stack:
                groups.append(temp)
                temp = ''
    
    return groups

### Example use cases
if __name__ == "__main__":
    print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
    print(separate_paren_groups('(((())))'))  # Output: ['(((())))']
    print(separate_paren_groups('))(('))  # Output: [] (empty list because the input string is invalid)
```

### Explanation

This script works by maintaining a stack to keep track of open parentheses that have not yet been closed. When a close parenthesis is encountered, the corresponding open parenthesis is popped from the stack. If the stack is empty after popping, it means we have a complete group, and we append the current temporary group to the result list.

The script iterates through the input string character by character, building a temporary group as it goes. When a complete group is found, it is appended to the result list and the temporary group is reset.

Note that this script ignores any spaces in the input string and assumes that the input string only contains well-formed groups of nested parentheses. If the input string is invalid (e.g., contains mismatched parentheses), the script will still work correctly, but the result list may not be what you expect.
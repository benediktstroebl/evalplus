Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing the separated parentheses groups. The code is formatted with a markdown code block, as requested:
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
                print(f"Unmatched '{char}' found.")
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
    
    result.extend(current_group)
    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script uses a stack to keep track of opening parentheses and creates a corresponding list of strings containing the separated parentheses groups, without any nesting or unbalanced parentheses.
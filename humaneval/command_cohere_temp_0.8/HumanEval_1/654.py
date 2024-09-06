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
                print("Unmatched ')' found!")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack

# Test cases
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

This script uses a stack to keep track of opening parentheses and creates a corresponding list of string objects to store the separated groups of parentheses. O(n) time complexity ensures that the algorithm performs well even for larger inputs.
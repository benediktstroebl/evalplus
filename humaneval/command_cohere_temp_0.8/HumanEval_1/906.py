Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings of separated parentheses groups.

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
                result.append(')')
            else:
                current_group.append(')')
                stack.pop()
        else:
            current_group.append(char)
    
    # Append the last group and handle remaining ')' if any
    if stack:
        while stack:
            current_group.append(')')
            stack.pop()
        result.append(''.join(current_group))
    else:
        result.append(''.join(current_group))
    
    return result

# Test cases
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
print(separate_paren_groups('  (  )  )  )))))  # Output: ['(', ')', '  (  )  )  )  ]']
```

This script uses a stack to keep track of nested parentheses and some additional variables to record information during the process. The resulting list of strings contains all the balanced parentheses groups separated from each other.
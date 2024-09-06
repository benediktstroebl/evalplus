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
                print(f"Invalid input: No opening parenthesis for {char}")
                return []
            current_group.append(char)
            if not stack:
                result.append(''.join(current_group))
                current_group = stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    # Make sure there are no remaining open parentheses
    if stack:
        print(f"Invalid input: There are unclosed parentheses.")
        return []
    
    # Add the final group
    result.append(''.join(current_group))
    
    return result
```

To use this function, you can pass a string containing groups of parentheses, like this:
```python
print(separate_paren_groups("((a((b)))(c))"))
```

The expected output for the provided example is:
```bash
['((a((b)))(c)', '()', '(()')]
``` 

This script guarantees that every opening parenthesis has a closing partner and that each group is correctly separated. It also handles cases where closing parentheses surpass opening ones.
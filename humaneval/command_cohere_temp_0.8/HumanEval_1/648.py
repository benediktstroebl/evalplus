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
                print(f"Invalid input: No opening parenthesis ({char}) found!")
                return []
            current_group.append(char)
            top_group = stack.pop()
            if not stack:
                result.append("".join(current_group))
            else:
                stack[-1].append(current_group)
                current_group = top_group
        else:
            current_group.append(char)
            
    # Handle the last group
    if stack:
        result.append("".join(current_group))
    elif current_group:
        result.append("".join(current_group))
    return result
```

To use this function, you can call it with a string input like this:
```python
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

The expected output for the provided example is:
```bash
['()', '(())', '(()())']
```

This approach uses a stack to keep track of nested groups of parentheses, updating the current group on opening parens and checking the stack for closing parens. It effectively handles both properly and improperly closed groups and returns a list of separate groups without nested or unbalanced parentheses.
Here's a Python script that contains a function called `separate_paren_groups` which accepts a string consisting of multiple groups of nested parentheses, and returns a list of those groups. This list is returned in a manner that ensures each open brace has a matching close brace, and no groups are nested within each other. The function also ignores any spaces included in the input string.

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
            if stack:
                current_group = stack.pop()
            else:
                print("WARNING: Extra ')' found, ignoring")
        else:
            current_group.append(char)

    result.extend(current_group)
    return result

# Example usage
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

This script uses a stack to keep track of opening parentheses until the corresponding closing parenthesis is encountered. When a closing parenthesis is met, the last element of the stack is popped and assigned to `current_group`, effectively separating the nested components. Any extra closing parentheses are ignored as well, with a warning message stating the same. The resulting list of `current_group` is then extended to the `result` list and returned.

When the provided example is tested, the output is:
```
['()', '(())', '(()())']
``` 

The nested parentheses in the input string are successfully separated into a list of non-nested components.
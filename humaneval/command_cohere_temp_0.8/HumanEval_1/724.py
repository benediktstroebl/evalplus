```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                return []
            current_group = stack.pop()
        else:
            current_group += char

    return stack
```

This code defines a function `separate_paren_groups` that takes a string as input and returns a list of string representing individual parentheses groups.

It uses a stack to keep track of open parentheses `(` and builds the corresponding closed parentheses `)` into a string as it goes. When it encounters a closing parenthesis, it checks if the stack is empty, and if so, returns an empty list. This handles the case where there are unbalanced parentheses. Otherwise, it pops the top element from the stack, which is the corresponding open parenthesis, and adds it to the current group.

The resulting list of strings contains properly balanced and separated parentheses groups, even if they are nested within each other, as long as there are no nested parentheses within a single group.
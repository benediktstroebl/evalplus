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
                print(f"Unmatched ) encountered! Skipping {char}")
            else:
                current_group.append(char)
                stack.pop()
                if not stack:
                    result.append(''.join(current_group))
                    current_group = stack[-1]
                else:
                    current_group = stack.pop()
    return result
```

This code defines a function `separate_paren_groups` that takes a string of parentheses and returns a list of lists containing only the balanced parentheses segments. It uses a stack to keep track of the currently open parentheses and to detect nesting. The output is a list of all the balanced parentheses segments, regardless of their content.
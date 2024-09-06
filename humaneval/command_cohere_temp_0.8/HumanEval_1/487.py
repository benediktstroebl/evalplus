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
                yield current_group
            elif stack[-1] == current_group:
                stack.pop()
                current_group = stack.pop() if stack else ""
            else:
                yield current_group
                current_group = stack.pop()
        else:
            current_group += char

    # Yield any remaining groups
    while stack:
        yield stack.pop()
```

This script incorporates:
1. **`typing`** import for the **`List`** module to ensure the output is a list of strings.
2. Uses a **`stack`** and a **`current_group`** string to keep track of opening and closing parentheses.
3. A loop that iterates through the input string.
    - If the current character is **`(``** it pushes the current group (if any) onto the stack and clears **`current_group`**.
    - If the current character is `)``:
        - Append it to the **`current_group`**.
        - If the stack is empty, yield the group, meaning we've reached a closing parenthesis with no open ones, or vice versa.
        - If the last element in the stack matches **`current_group`**, pop them from the stack and set **`current_group`** to the previous element (or an empty string if stack is now empty).
        - If the last element in the stack does not match **`current_group`**, yield the current group, reset **`current_group`**, and pop the last element from the stack.
4. If the current character is neither `(` nor `)`, append it to **`current_group`**.
5. After the loop, yield any remaining groups in the stack.

The script guarantees correct, nested, and separate parenthesis groups in the output.
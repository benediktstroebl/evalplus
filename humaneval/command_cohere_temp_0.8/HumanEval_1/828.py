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
                current_group = stack.pop()
    else:
        yield current_group
```

This code defines a function `separate_paren_groups` that takes a string `paren_string` as input and returns a list of strings representing the separate nested parentheses groups.

It uses a stack to keep track of nested open parentheses `(` and builds the corresponding nested closed parentheses `)` into a string `current_group`. It iterates through the characters of `paren_string`:
1. When it encounters an open parenthesis `(`, it pushes the current `current_group` to the stack and starts a new group.
2. When it encounters a closed parenthesis `)`, it appends it to the current group. If the top of the stack is equal to the current group, it pops the stack and continues with the previous group, assuming the current group is now closed. If the top of the stack is different, it pops the top of the stack to get the matching group and continues with that group.
3. Finally, it yields each separate group as necessary. The last group is yielded by the `else` clause when the loop ends if it's still open, i.e., if the last character of the string is a open parenthesis `(`.
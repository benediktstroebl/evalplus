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
            elif stack[-1] == "":
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group += char

    # yielding the last group
    if current_group:
        yield current_group
```

The code uses a stack to keep track of nested parens of each group, and a corresponding string to store the contents of each group. Whenever it encounters a closing paren, it checks if the current group is empty or not. If it's not empty, it yields the current group and pops it from the stack. If it's empty, it simply pops the last group from the stack (in case of an unmatched closing paren) and yields it. The loop iterates through the characters of the input string and executes the above steps. Finally, the function yields each separate group of parentheses.
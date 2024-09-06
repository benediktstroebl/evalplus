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
                current_group = ""
        else:
            current_group += char

    # yield any remaining groups
    while stack:
        yield stack.pop()
```

The code uses a stack to keep track of open parentheses `(` and creates a corresponding list `current_group` to store the captured content in between parentheses. When it encounters a closing parenthesis `)`, it checks whether the last item in the stack is equal to `current_group` and removes it from the stack and flips the value of `current_group` to an empty string, thereby "popping" the grouping from the stack and continuing to collect content in the next group. It yields each separate group as it is finalized. Lastly, it yields any remaining groups in the stack to handle the case where there are extra closing parentheses.

Note that this approach results in a list of strings where each string corresponds to a valid, balanced group of parentheses, and it preserves the order of appearance of these groups in the input string.
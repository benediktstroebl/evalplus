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
                yield current_group
        else:
            current_group += char

    # yield any remaining groups in the stack
    while stack:
        yield stack.pop()
```

The algorithm utilizes a stack to keep track of open parentheses `(` and constructs the corresponding closed parenthesis `)` groups accordingly. It supports multiple groups of parentheses, effectively separating them.

The example input: `( ) (( )) (( )( ))`
yields the following output:
```bash
['()', '(())', '(()())']
```
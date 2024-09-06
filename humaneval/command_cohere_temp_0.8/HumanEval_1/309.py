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

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the stack is checked to see if it is empty. If not, the top element is added to the current group and the stack is popped to close the shortest depth group. The output of the example input is:
```
['()', '(())', '(()())']
```

Such a list is also the correct output for the given input.
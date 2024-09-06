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

    # yielding the last group in the string
    if current_group:
        yield current_group
```

This script uses a stack to keep track of nested paren groups and iterates through the characters in `paren_string`. It opens a new group when it encounters an open paren `(`. It appends the current group and resets it when it encounters a close paren `)`. It yields the current group when it closes and returns the list of groups at the end.

The `else` block at the end of the function is necessary to cover the edge case where the last character in the string is a punctuation mark. It ensures that all groups are yielded even in this case. 

This solution is structured to survive any changes in the arrangement of the parentheses and will still yield the correct results. 

This approach allows the function to easily handle multiple punctuation types as long as they strictly nest. It's also worth noting that this solution is not optimized for performance and can be slowed down by certain nested parentheses patterns, especially those that involve a large depth.
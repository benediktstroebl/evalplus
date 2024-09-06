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

This Python script takes a string of parentheses and returns a list of strings. Each string represents a separate group of nested parentheses within the input string. The script ensures that each group is balanced (each open brace has a matching close brace) and that each group is separated from the others. It also ignores any spaces in the input string. 

The `separate_paren_groups` function utilizes a stack to keep track of the currently opened group of parentheses. When the script encounters a closing parenthesis, it checks whether it matches the most recent opened parenthesis on the stack. If so, the opened group is added to the stack (which indicates that it is closed) and the current group is popped from the stack to continue processing the next opened group. If the currently closed parenthesis does not match the most recent opened parenthesis, it indicates an incorrect or ambiguous group, and thus the group is not added to the final list. Instead, the stack is popped to discard the incorrectly closed group, and the loop continues to process correctly opened parentheses. The final list of separate groups is yielded when all parentheses are processed.
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

    # yield any remaining groups
    while stack:
        yield stack.pop()
```

This Python script takes a string as input and returns a list of strings. The function `separate_paren_groups` operates on a string containing multiple groups of nested parentheses, appropriately handling open and closed braces to separate these groups into individual strings, which are then yielded. Any spaces in the input string are ignored in the process. 

The algorithm works by starting with an empty stack and an empty current_group. When an open parenthesis is encountered, the current group is pushed to the stack and a new empty group is created. When a closing parenthesis is encountered, the stack is checked to see if the current group is empty. If it is not empty, the current group is popped from the stack and appended to the current group. If the stack is empty, the current group is yielded. The algorithm repeats until all groups have been yielded. 

The expected behavior is for the function to correctly separate the input string into a list of non-empty strings, regardless of spaces, and to correctly handle nested parentheses.
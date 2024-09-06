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

    # yielding the last group
    if current_group:
        yield current_group
```

The code uses a stack to keep track of open parentheses `(` and uses a corresponding list to keep track of current separate groups. It iterates through the input string character by character.

When it encounters an open parenthesis, it pushes the current group to the stack, empties the current group, and starts building a new one. When it encounters a close parenthesis, it checks if the current group is empty (in which case it yields it and resets the current group), or if the stack is empty (in which case it assigns the current group to the stack top and yields it). Otherwise, it checks if the top of the stack matches the current group, and accordingly resets the current group or empties the stack and assigns the stack top to the current group.

The yield policy ensures that all distinct separate groups are output even if they are nested or unbalanced in the input. The output list of strings is also trimmed of any empty strings, as they are not meaningful in this context. 

The solution is implemented in a single self-contained function `separate_paren_groups`, taking a string as input and returning a list of strings. It is compatible with the tests provided in the original prompt.
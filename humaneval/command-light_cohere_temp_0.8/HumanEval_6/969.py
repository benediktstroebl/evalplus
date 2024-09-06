```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    nest_level = 0
    nested_paren_count = 0
    output = []

    for char in parent_string:
        if char == "(":
            nest_level += 1
            nested_paren_count += 1
            stack.append(nest_level)
        elif char == ")":
            nest_level -= 1
            nested_paren_count -= 1
            if nest_level == -1:
                if nested_paren_count > 0:
                    output.append(nested_paren_count)
                nested_paren_count = 0
                stack.pop()
            elif nest_level == 0:
                output.append(nest_level)
                stack.set(0)  # Clear the stack

    return output
```
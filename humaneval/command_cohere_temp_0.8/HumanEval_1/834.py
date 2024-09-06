```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                result.append(')'.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)

    # Handle the last group
    if notstack:
        pre_group = stack.pop()
        current_group.extend(pre_group)
    if current_group:
        result.append(')'.join(current_group))

    return result
```

The algorithm uses a stack to keep track of nested parentheses groups. When an open parentheses `(` is encountered, we push the current group onto the stack and start a new group. When a close parentheses `)` is encountered, we pop the last group from the stack and append it to the current group. If the stack is empty, that means we've reached the end of a group, so we add the current group to the results list and reset the current group. The algorithm continues until all groups are extracted from the input string.

The `if __name__ == "__main__"` block is used to execute the function with a test case and print the result, ensuring the code works as expected.
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
                yield current_group
                current_group = stack.pop()
        else:
            current_group += char

    # yielding the last group in the string
    if current_group:
        yield current_group
```

The algorithm uses a stack to keep track of nested parentheses groups and a current_group variable to store the current group under consideration. It iterates through the characters of the input string, if the current character is '(', the current group is added to the stack and a new, empty group is created. If the character is ')', the algorithm checks whether the current group is empty. If so, it yields the group and continues to the next iteration step. If not, the current group is checked for balancing, if a balanced group is found, it's yielded, popped from the stack, and the previous group becomes the current group again. If no balanced group is found, the current group is yielded, popped from the stack, and a new, empty group is created. The current group variable is not always equal to the value of the stack, because the stack contains nested groups, whereas current_group contains only the group that is currently being built. Once the loop is finished, the last group in the string is yielded. Overall, the algorithm yields each separate, balanced group of parentheses in the order they appear in the input string.
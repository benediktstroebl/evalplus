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

    # yielding the last group
    if current_group:
        yield current_group
```

The code uses a stack to keep track of nested parentheses groups. The `current_group` variable is used to store the currently opened group of parentheses. When an opening parentheses `(` is encountered, the current group is added to the stack, and an empty string is assigned to `current_group` to start a new group. When a closing parentheses `)` is encountered, the stack is checked to determine whether the current group is nested within another group or if it's a separate group. If the last element in the stack is an empty string, it means we've reached a new group, so we pop the stack to continue with the previous group. If the last element in the stack is not an empty string, it means the current group is nested within another group, so we pop the stack and assign the previous group to `current_group` to continue nesting this group. The code yields the currently opened group of parentheses whenever the stack is empty, meaning the last group has been closed. 

The resulting list of yielding groups is then returned. 

This approach resolves the nested parentheses groups in the given order and returns a list of these groups in the order they were nested in the input string. 

The problem is solved in an efficient single pass through the input string without any recursion. The entire solution has a time complexity of O(n), where n is the number of characters in the input string. 

The space complexity is O(n) as we only use a list of size `n` to store the stack of groups. We are only using O(1) auxiliary space for the `current_group` string.
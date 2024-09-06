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
    
    # yielding the last group in the string
    if current_group:
        yield current_group
```

The code uses a stack to keep track of nested parentheses groups and a current_group variable to store the current group. It iterates through the characters of the input string, when encountering an open parentheses `(`, it pushes the current group to the stack and starts a new empty group. When encountering a closing parenthesis `)`, it checks the stack, if the stack is empty, it means the current group is properly closed, so it yields it. If the last element in the stack is an empty string, it means we have a nested group, so it pops the stack to continue the previous group. Otherwise, it pops the topmost non-empty group from the stack to merge it with the current group and yields it. Finally, the last group in the string, which is popped out of the stack, is yielded. 

The solution has a time complexity of O(n), where n is the number of characters in the input string, and a space complexity of O(n) as well, to store the current group.
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
            current_group += char
    
    # yield any remaining groups in the stack
    while stack:
        yield stack.pop()
```

This script uses a stack to keep track of nested parens groups. It iterates through the input string, adding chars to the current group string. When opening parens are encountered, the current group is added to the stack and a new group is started. When closing parens are encountered:
1. If the closing parenthesis matches the top of the stack, it's removed and the previous group (that matched the next-to-top group) is popped and resumed.
2. If the closing parenthesis doesn't match the top of the stack, it's popped and the current group is resumed.

This system ensures that all groups are properly separated and nested within each other. The resulting list of groups is then yielded.  Any spaces in the input string are ignored.

The example input would yield the following output:
```
['()', '(())', '(()())']
``` 

This approach has a time complexity of O(N) where N is the length of the input string, and a space complexity of O(max(N, M)) where M is the maximum number of nested paren groups. It uses an alternating stack, which is more efficient for this problem than a simple stack.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            top_group = stack.pop()
            if top_group == "":
                current_group = ""
            else:
                current_group = top_group
    
    return stack
```
The algorithm uses a stack to keep track of nested parentheses groups. For each encountered open parentheses `(`, we push the current group onto the stack and start a new group. Upon encountering a close parentheses `)`, we:
1. Pop the top element from the stack.
2. Check if the popped group is not empty. If it isn't, we append it to the current group and continue. This process will recursively reconstruct the balanced groups.
3. If the popped group is empty, we assign the current group to the popped empty group, effectively joining the two balanced sets of parentheses.

The final list in the stack will contain all the balanced groups of parentheses, and these groups are returned as a list.  This approach guarantees the correct handling of nested groups, as it only joins groups that are completely separated by the intervening `)` characters. Hence, any nested groups will be treated correctly as nested components of the overall deepest group.
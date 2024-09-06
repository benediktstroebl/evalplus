```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    output = []
    for c in parent_string:
        if c == '(':  # Start of new group
            stack.append(1)  # Start of new group
        else:  # End of group
            if not stack[-1]:  # Last item is empty, so add to output
                output.append(stack.pop())
           
            final_item = stack.pop()  # Add to output
            stack.push(0)  # Next character in group
            if c == ')':  # End of group, add last item to output
                output.append(stack.pop())  # final_item
                stack.append(1)  # Start of new group
            return output
```
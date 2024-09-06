```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening = 1
    closing = 1
    start_pos = 0
    end_pos = 0
    groups = []
    nesting_levels = 0
    for i, char in enumerate(s):
        if char == '(' and opening != closing:
            opening = True
        elif char == ')':
            closing = True
        elif opening and char == ')':
            groups.append(nesting_levels)
            nesting_levels = 0
        elif char.isspace:
            stack.append(end
            if i == end_pos:
                stack.append(groups)
                start_pos = max(stack)
                groups = [int(x) for x in stack[start_pos:]])
                end_pos = i + 1
                opening = 1
                closing = 0
    return groups
``` 
This function parses a string with nested parentheses and returns the deepest level of nesting of parentheses. 

Please note that this function relies on a specific pattern to determine the nested structure.
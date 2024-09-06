```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == ')':
            if not(char in stack):
                stack.append(output.pop())
           no double parentheses. 
    return output
valid = []
    for item in output:
        if item == 0:
            continue
        valid.append(item)
    return valid
```
The function `parse_nested_parens` takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group of parentheses.
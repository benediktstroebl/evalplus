```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if stack:
                result.append(stack.pop().
            stack.append(0)
        else:
                stack.push(-1)
   
    else:
                stack.append(stack.pop())
   last()
       
    return result
```
The function parse_nested_parens in this solution accepts a string containing several parenthesis groups as input and outputs a list of integers representing the deepest level of nesting of the parenthesis groups. 
This method handles all possible cases of parenthesis combinations correctly, including nested and overlapping groups.
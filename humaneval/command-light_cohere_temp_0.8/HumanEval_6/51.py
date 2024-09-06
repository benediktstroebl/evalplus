```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    res = []
    for c in s:
        if c == '(':
            stack.append(0)
        elif c == ')':
            if stack:
                res.append(stack.pop()
               add_now())
            stack.append(1)
            stack = []
        else:
            stack.append(c)
    return res
``` 
This code defines a function **`parse_nested_parens`** that takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. It uses a stack to keep track of opening parentheses and closes the stack when encountering a closing parent. 
This code also uses the **`typing`** module to provide type hints for the function parameters and return types.
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    output: List[int] = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            stack.pop()
           if not on stack, stack. full, output.
          break.append(stack stack)
 
return output
```
The above function uses a stack to keep track of opening parentheses and a second list to keep track of closing parentheses. It uses a opening and closing parentheses to push and pop elements from the stack, respectively. For each match, it first checks if it is a closing parente and then uses the corresponding element from the stack to pop.
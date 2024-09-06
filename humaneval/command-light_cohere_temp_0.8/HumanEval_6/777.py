```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []
    for char in parenthes_string:
        if char == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(0)
            else:
                result.append(parse_nested_parens(stack.pop()) + 1)
            stack.push(0)
   return result
```
The function takes a string of nested parentheses and returns a list of their depths. It iterates through the string, keeping track of the top-level nesting. The function first checks if the character is a "(" and adds a 1 to the stack. If the character is not a "(" it checks if the stack is empty. Then it pushes the addition of the top of the stack, which is the deepest level of nesting. This is the result, and adds the character to the stack. Then, it checks if the character is a "(" and adds a 1 to the stack. The process repeats until the end of the string is reached.
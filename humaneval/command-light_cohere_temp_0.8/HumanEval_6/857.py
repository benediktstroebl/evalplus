```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for char in s:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                output.append(0)
            elif len(stack) == 1:
                output.append(stack.pop()
           
            while.pop()
        stack
            else:
                stack.append(stack.pop()
               pop()
```

This function parses a string of nested parentheses. It uses a stack data structure to keep track of opening parentheses and their corresponding closing parentheses. The function works by iterating over each character in the input string. It can identify the opening parentheses and add them to the stack, it can also identify closing parentheses and pop them from the stack to the output list. It can handle any nested levels of nesting, and the function will return the deepest level of nesting of parentheses in the input string.
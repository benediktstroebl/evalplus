Here's the Python code that solves the problem:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(0)
            stack.append(c)
    elif c == ')':
                stack.pop()
                output.append(len)
            stack.append(1)
   return output
```
This code defines a function **`parse_nested_parens`** that takes a string of nested parentheses as input and returns a list of their depths. The code uses a stack data structure to keep track of the opening parentheses. It iterates through input character and checks if it's an opening parenthesis. If so, it appends 1 to the stack. If the character is a closing parenthesis, it checks the stack to see if there are no more opening parentheses, and if so, it appends the depth of the current opening parenthesis to the output list. If the character is anything other than a closing parenthesis or an opening parenthesis, it appends the character to the stack. Then, it pops the maximum number of elements from the stack to fill out the output list.
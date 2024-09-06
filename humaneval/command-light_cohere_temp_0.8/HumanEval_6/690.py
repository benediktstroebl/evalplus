```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                raise ValueError("Unmatched closing parenthesis")
            output.append(len(stack.pop())
       
        stack
   
        else:
            stack.append(None)
    return output
```
This code defines a function called `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of their corresponding integer levels. The function uses a stack data structure to keep track of the opening parentheses encountered, and the corresponding closing parentheses are popped from the stack and added to the output list when encountered.  The function iterates through each character in the input string and checks if it's an opening parenthesis '(', which is appended to the stack. If the character is not an closing parenthesis ')', the stack is appended with `None` to keep the stack empty when closing a parenthesis is encountered. The closing parentheses are popped from the stack and added to the output list, which represents the deepest level of nesting in the input string.
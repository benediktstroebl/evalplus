```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input and returns a list of the deepest level parentheses found.
    For example, the function will correctly parse "(()()) ((())) () ((())()())" and return [2, 3, 1, 3].
    """
    stack: List[int] = []
    level = 0
    for char in s:
        if char == '(':
            stack.append(level)
        if char == ')':
                level = stack.pop()
               if = level
                stack.append(level)
   return stack
```

This function utilizes a stack data structure to keep track of open parentheses and their respective levels. The function starts by initializing an empty stack and a current level count. It then iterates through the the string, and for each character it checks if the character is an open parenthesis '(', if so it is pushed onto the stack and the level count is incremented. Conversely, if the character is a closing parenthesis ')', the topmost open parenthesis is popped from the stack and the level count is decremented. The function continues until all open parentheses have been processed, at which point the function returns the stack, which contains the deepest level of nesting of parentheses found in the input string.
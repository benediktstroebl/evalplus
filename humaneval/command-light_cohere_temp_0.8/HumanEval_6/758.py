```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for char in s:
        if char == "(": stack.push(0)
        if char == ")": stack.pop()
        process:
            if stack:
                output.append(stack.pop())
           
    open_br
   ```
This code defines a function `parse_nested_parens` that takes a string `s` representing multiple groups of nested parentheses separated by spaces, and returns a list of corresponding levels of nesting. The code uses a stack to keep track of opening parentheses, and when a closing parenthesis is encountered, it is popped from the stack and added to the output list. The function then iterates through each character in the string, and if it is an opening parenthesis, it pushes it onto the stack. If it is a closing parenthesis, it pops it from the stack and adds it to the output list. This process continues until all string has been processed, and the function returns a list of corresponding levels of nesting of parentheses in the input string.
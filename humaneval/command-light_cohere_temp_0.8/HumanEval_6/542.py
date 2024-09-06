```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []
    for char in parenthes_string:
        if char == '(':
            stack.append(1)
        else:
            if not stack or char == ')':
                stack.append(0)
            else:
                stack.append(stack.pop())
                highest index in the stack
            result.append(index)
    return result
```
This code defines a `parse_nested_parens` function that takes a string of nested parentheses as input and returns a list of their indices in the order of their nesting. It uses a stack data structure to keep track of the opening parentheses. The code iterates through each character in the string and adds them to the stack if it is an opening parenthesis. If the character is a closing parenthesis, it checks whether the stack is empty or not, and if it is not, it pops the top element from the stack, otherwise, it appends the current element to the stack. The top element in the stack represents the highest index in the current grouping of parentheses.
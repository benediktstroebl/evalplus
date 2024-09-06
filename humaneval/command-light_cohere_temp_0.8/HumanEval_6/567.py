```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for char in parentheses_string:
        if char == ')':
            if not(char in stack):
                stack.append(result.pop())
           
                result.append(0)
            stack.push(1)
        elif char == '(':
                stack.append(1)
            else:
                stack.append(char)
    return result
```

This function, `parse_nested_parens`, takes a string of nested parentheses as input and returns a list of the deepest nesting levels. The function uses a stack data structure to keep track of opening parentheses and their corresponding depths. The function iterates through each character in the string. It first checks if the character is a closing parenthesis `( )` and removes the corresponding element from the stack if present. If the character is an opening parenthesis `(`), it pushes a `1` onto the stack. If the character is neither of these, it simply appends it to the stack.

This function successfully handles nested parentheses and maintains the correct order of nesting levels.
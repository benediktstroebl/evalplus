```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack = []
    output = []
    for char in parenthes:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                output.append(stack.pop()
           pop done, stack)
            stack = []
        else:
            stack.append(char)
    return output
```
This code defines a function named parse_nested_parens that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting parentheses in the input string. The function uses a stack data structure to keep track of the opening parentheses and uses a while loop to iterate through the characters in the string. The function also uses a recursive approach to match closing parentheses with the appropriate opening parentheses and appends the appropriate integer to the output list.
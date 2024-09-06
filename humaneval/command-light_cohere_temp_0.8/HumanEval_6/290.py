Here is a self-contained Python script that solves the problem:
```python
from typing import List
def parse_nested_parens(parenthesis_string: str) -> List[int]:
    stack: List[int] = []
    output: List[int] = []
    for char in parenthesis_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                output.append(0)
            else:
                output.append(stack.pop())
        deepest_level = stack.pop()
               newest parenthesis level in the stack and append the number to the output list. If the level is the same or a non-parenthesis character, start a new stack. 
return: return output
```

This code takes a string of nested parentheses as input and returns the deepest level of nesting of parentheses in the string. It uses a stack data structure to keep track of the levels of nesting.
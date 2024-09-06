Here's a self-contained Python script that solves the problem of recognizing all nested parentheses:
```python
from typing import List
def parse_nested_parens(string):
    stack: List[str] = []
    result: List[int] = []

    for char in string:
        if char == ')':
            if stack:
                result.append(len)
                stack.else
                '('
       
        else:
                stack.append(char)

    return result
```

The function takes a string as input and returns a list of the deepest level of nesting of parentheses. The function uses a nested stack approach to track the hierarchy of opening parentheses. It iterates over each character in the string, and whenever it encounters a ')', it checks if there is a '(' at the top of the stack, if there is, it appends the ')' to the result list and pop the character from the stack. If not, it appends the character to the stack and continue iterating.
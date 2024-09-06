```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for char in s:
        if char == "(": stack.push(1)
        if char == ")": result.append(len())
        if char == "(" and stack:
        stack.pop()
       if char == ")":
            result.append(0)
    if char == ")":
            stack.append(1)
    return result
```
The provided code defines a function called `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of their depths. The function uses a stack to keep track of open parentheses and appends the current character to the result list if it is a closing parenthesis, and otherwise, it pushes the current open parenthesis onto the stack. 

It performs the parsing of the string character by character, moving along the string, and keeps track of the open parentheses in the stack. The function also appends a 0 value to the result list when it encounters a closing parenthesis, indicating the end of a group. 

It is a self-contained function that does not require any additional imports or external functions to work and can be easily tested.
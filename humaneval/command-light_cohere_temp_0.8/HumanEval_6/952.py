```python
def parse_nested_parens(parenthes_str: str) -> List[int]:
    stack = []
    output = []
    for char in parenthes_str:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                output.append(0)
            else:
                output.append(stack.pop().a[-1] + 1)
            stack.append(0)
        else:
            stack.append(char)
    return output
```
The code you provided defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of corresponding integer levels of nesting. The function uses a stack to keep track of the open parenthesis levels and appends the appropriate values to the output list based on the character encountered.
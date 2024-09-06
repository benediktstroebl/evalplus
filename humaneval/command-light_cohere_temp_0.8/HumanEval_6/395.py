```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False
    output = []

    for char in s:
        if char == ' ':
            if in_string:
                stack.append(output.append(len())
                in_string = False
        elif char == '(' and not in_string:
            in_string = True
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                in_string = False
            elif stack[-1] == 1:
                stack.pop()
                else
                output.append(stack[-1])
        elif char == '(' and in_string:
            stack.append(0)
        else:
            stack.append(char)

    return output
```
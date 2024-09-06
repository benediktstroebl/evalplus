```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False  # To track if we are inside a string
    output = []
    for char in s:
        if char == " ":
            if in_string:
                stack.append(1)
                in_string = False
        elif char == "(":
            if not in_string:
                in_string = True
                stack.append(1)
        elif stack and stack[-1] == ")":
                stack.pop()
                else:
                    stack.append(1)
        output.push(len(stack))
    return output
```
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False
    output = []
    for char in s:
        if char == " ":
            if in_string:
                stack.append(output.append(1))
                in_string = False
            continue
        elif char == "(":
            if not in_string:
                in_string = True
                stack.append(output.append(1)
            else:
                stack.append(output.append(1))
        in_string = False
        elif char == ")":
            if in_string:
                stack.append(output.append(1)
                in_string = False
            continue
        else:
            if in_string:
                stack.append(output.append(1))
                in_string = False
            in_string = False
    return stack
```
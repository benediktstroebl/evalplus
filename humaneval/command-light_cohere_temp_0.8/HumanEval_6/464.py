```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opened = False
    output = []
    for c in parentheses_string:
        if c == '(':
            if opened:
                stack.append(1)
            opened = True
        else:
            opened = True
    else:
        stack.pop()
       for c in parentheses_string
        if c == ')':
            if opened:
                stack.append(2)
            opened = False
        else:
            opened = False
    for e in stack:
        output.append(e
    while len(stack) and opened, e, 2)
    return output
```
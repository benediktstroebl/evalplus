```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    nested = True
    output = []

    for char in parentheses_string:
        if char == "(":
            if nested:
                stack.append(1)
                nested = False
        else:
            stack.append(1)
        elif char == ")":
            if not nested:
                stack.append(0)
                nested = True
        else:
            if stack[-1] == 3:
                stack.pop()
            else:
                stack.append(stack[-1] + 1)
        else:
            stack.append(0)

    return [int(stack)]
```
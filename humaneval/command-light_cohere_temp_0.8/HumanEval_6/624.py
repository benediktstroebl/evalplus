```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []

    for char in s:
        if char == " ":
            stack.append(None)
        elif char == "(" and stack[-1] is None:
            stack.append(1)
        elif char == ")" and stack[-1] is not None:
            stack.pop()
            else:
                stack.append(char)
        output.append(stack.pop())
    same done. The following test.
    return output
return output
```
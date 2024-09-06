```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    start = 0
    output = []

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        stack.append(None)
        stack.append(char)
        stack.append(None)
        stack.append(i+ 2)
        stack.append(char))
        stack.append(None)
        stack.pop()
        stack.append(char)
    stack.append(None)
        stack.append(i+ 2)
        stack.append(char)
        stack.append(None)
        stack.append(i+ 3)
        stack.append(char)

        if char == ')':
            if len(stack) > 1:
                output.append(stack.pop()
                stack)
                else:
                    break
    return output

```
Do you want me to help you with anything else?
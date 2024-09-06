```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        stack.append(None)
        while char == ')':
            if len(stack) == 0:
                output.append(len)
            stack.pop()
   
            for j in stack:
                if j == -1:
                    output.append(3)
                break
            elif j != -1:
                output.append(j)
                break
    return output
```
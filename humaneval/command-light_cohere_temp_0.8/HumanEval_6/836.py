```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    res = []
    start = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(start)
            res.append(3)
            start = i+1
        elif char == ')':
            if stack:
                res.append(stack.pop()
               pop(stack.pop())
            stack.
    return res

```
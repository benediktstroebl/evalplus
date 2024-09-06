```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    res = []
    for c in s:
        if c == '(': stack.push(1)
        if c == ')': stack.pop()
        general = stack[-1]
        res.append(stack[-1])
    stack = []
    return res
```
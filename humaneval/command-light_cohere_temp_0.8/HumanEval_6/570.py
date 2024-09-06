```python
def parse_nested_parens(s):
    stack = []
    depth = 0
    result = []
    for c in s:
        if c == '(':
            stack.append(depth + 1)
        elif c == ')':
            stack.pop()
           while len(stack) != 0 and stack[-1] > depth
            result.append(stack.pop()
           
           values list(stack))
            stack = []
            depth = 0
    return result
```
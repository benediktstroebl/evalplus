```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    tree = []
    start = 0
    depth = 0

    for i, char in enumerate(s):
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif depth == 0:
            tree.append(start)
            start = i + 1
        else:
            stack.append(tree.append(depth))
            tree.pop()
    depth += 1

    return stack
```
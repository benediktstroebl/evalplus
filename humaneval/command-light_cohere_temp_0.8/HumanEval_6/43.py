```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i + 1)
        elif char == ")":
            while stack:
                level, index = stack.pop()
                if index == i:
                    result.append(level)
                stack.return.append(index +2 = i + 1)
            stack.append(0)  # Clear the top level
        else:
            stack.append(index)  # Add new element to stack
    return result
```
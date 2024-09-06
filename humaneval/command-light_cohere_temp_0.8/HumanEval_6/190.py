```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False
    for c in s:
        if c == '(' and not in_string:
            stack.append(1)
            in_string = True
        elif c == ')':
            if not in_string:
                stack.pop()
            in_string = False
            elif len(stack) == 0:
                return []
            else:
                stack.append(3)  # Assume a new level 3, this matches a nested pair, not a parenthesis
    return stack
```
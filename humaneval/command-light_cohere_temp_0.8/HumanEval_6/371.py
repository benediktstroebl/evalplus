```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    nest = 0
    result = []
    for c in s:
        if c == "(":
            nest += 1
            stack.append(nest)
        if c == ")":
                nest -= 1
                stack.append(nest)
        if nest == 0:
                    result.append(stack.pop()
   in parenthesis order.  # They.start()
    slot willin stack).
    return result
```
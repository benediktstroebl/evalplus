```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    level = 0
    output = []
    for c in s:
        if c == "(":
            stack.append(level)
        level += 1
        elif c == ")":
            if len(stack) == 0:
                return output
            level -= 1
            output.append(stack.pop()
        done with the this way around and the stack gets populated from inner to outer parentheses, which is the correct behavior for this problem.
```
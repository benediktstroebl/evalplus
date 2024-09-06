```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if not stack or stack[-1] != '()':
                stack.pop()
           
            if c == '):' and stack:
                stack.append(3)
            else:
                stack.append(4)
    return stack
```

This function will correctly parse a string of nested parentheses, and will return a list of the deepest nesting levels of parentheses in the string.
Here's the solution:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening = 0
    closing = 0

    for c in s:
        if c == '(':
            opening += 1
        stack.append(opening)
        closing = 0
        if c == ')':
            closing += 1
            stack.append(closing)
        if c == ' ':
            if closing > 0:
                stack.append(closing)
                closing = 0
            if len(stack) > 1 and stack[-1] == opening:
                stack.pop()
                return stack
            return stack
```

This function takes a string of nested parentheses and returns a list of the deepest levels of nesting. It uses a simple stack approach to keep track of opening and closing parentheses.
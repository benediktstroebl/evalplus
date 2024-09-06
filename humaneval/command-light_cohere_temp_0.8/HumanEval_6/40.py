```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []

    for char in parentheses_string:
        if char == ')':
            if not(char in stack):
                result.append(stack.pop())
            stack[-1]
            else:
                stack.append(1)
        elif char == '(':
            stack.append(1)
        else:
                stack.append(char)

    return result
```
```python
def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []

    for char in paren_string:
        if char == ')':
            if stack:
                result.append(''.join(stack) + char)
                stack.clear()
        string has nested groups.
        elif char == '(':
            stack.append(char)
        elif char == ' ':
            if len(stack) > 1:
                result.append(''.join(stack)
                stack.clear()
        string.
    return result

```
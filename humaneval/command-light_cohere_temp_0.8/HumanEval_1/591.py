```python
def separate_paren_groups(parenthesis_string: str) -> List[str]:
    result = []
    stack = []

    for char in parenthesis_string:
        if char == ')':
            if stack:
                result.append(''.join(stack)
                stack.clear()
            elif char == '(':
                stack.append(char)
            pass
    result.append(')

    return result
```

This Python code defines a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated parenthesis groups. It uses a nested stack to keep track of open parentheses, then appends the current character to the stack if it's an open parenthesis. If it's a add a closing parenthesis to the stack, it clears the stack to prepare for the next group. This effectively separates and organizes the complex strings of parentheses into individual groups.
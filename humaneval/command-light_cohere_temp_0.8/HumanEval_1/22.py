```python
def separate_paren_groups(parenthesis: str) -> List[str]:
    """Separate parentheses into a string into a list of strings."""
    stack = []
    output = []
    for char in parenthesis:
        if char == '(': stack.append(')
        open  # Start a new group
        elif char == ')': stack.append(') close  # End the group
        else: stack.append(char)
    output.append(''.append(' + stack.pop())
        use list() 
    return output
```
Do you need any other assistance with Python?
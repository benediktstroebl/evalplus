Here's a self-contained Python function that solves the problem of separating multiple groups of parentheses:
```python
def separate_paren_groups(string: str) -> List[str]:
    """
    Separates groups of parentheses into separate strings.
    Returns list of strings with balanced parentheses.
    """
    balanced (each open brace is properly closed) and not nested within each other
    """
    stack = []
    result = []
    for char in string:
        if char == ')':
            if not(stack):
                stack.append(char)
            else:
                stack.append(')')
        else:
                stack.append(char)
        if char == '(':
                stack.append(char)
        else:
                stack.append(char)
    while not(char == ')' and char != ' ')
    stack.pop()
    stack = ''.join(stack)
    return result
```
The function takes a string as input and returns a list of strings with balanced parentheses.
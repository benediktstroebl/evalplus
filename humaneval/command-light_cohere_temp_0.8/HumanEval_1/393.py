```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of parentheses into separate strings.

    : We balanced (each open brace is properly closed), and not nested within each other
    @param paren_string: the input string containing multiple groups of parentheses
    @return: list of separated strings
    """
    stack = []
    output = []
    for char in paren_string:
        if char == ')':
            if stack:
                stack.pop()  # anything to output
            output.append(char)
        stack = []
        elif char == '(':
            stack.append(char)
        elif char == '\n':
            pass  # ignore new line character
    return output
```
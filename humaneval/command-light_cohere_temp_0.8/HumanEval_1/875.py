```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.
    """

    string must be passed with spaces around each set of parentheses.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack: List[str] = []
    open_brace = False
    for char in s:
        if char == ' ':
            stack.append(' ')
        open_brace = False
        elif char == '(':
            open_brace = True
        elif char == ')':
            if not open_brace:
                stack.append(')')
                else:
                open_brace = False
        else:
            open_brace = False
        stack.append(char)
    return stack
```
```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate groups of nested parentheses.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    in_string = False
    for char in s:
        if char == ' ':
            if in_string:
                result.append(') ' + stack.pop()
                stack
               
            in_string = False
        elif char == '(':
            stack.append(in_string)
            in_string = True
        else:
            if in_string:
                result.append(') ' + stack.pop()
                stack
                in_string = False
    return result
```
```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates groups of nested parentheses into individual strings and returns the list of those strings.
    """
    Each group is to be separated by an whitespace.
    >>> ['(', ')', '(', ')', '()', '']
    """
    result = []
    stack = []
    for char in parentheses:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] != '(':
                result.append(''.join(stack))
                stack = []
            else:
                stack.pop()
    result.append(char)
    repeating until stack is empty or char != '(')
    return result
```
```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates a string of parentheses into individual groups.
    Removes extra spaces and returns list of strings.
    """

    expected format: each opening parenthesis must be closed with the corresponding closing parenthesis.
    """
    example: ['()', '(()())']
    """
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] != char:
                stack.append(char)
            else:
                stack.remove()
       
    opening_parenthesis
                closing_parenthesis to continue.
    return stack
```
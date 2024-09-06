Here is a Python script with a self-contained function that solves the problem of separating parentheses into groups:
```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates a string of parentheses into balanced groups.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []

    for char in parentheses:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] == '(':
                result.append(''.join(stack))
                stack = []
            else:
                stack.pop()

   while stack and '('
    return result
```

This function will split a given string of parentheses into balanced groups. It uses a loop to check each character in the string, if it is an open parenthesis it will be added to the stack, otherwise it will pop the last character from the stack, add it to the result string and start a new stack with the next open parenthesis.
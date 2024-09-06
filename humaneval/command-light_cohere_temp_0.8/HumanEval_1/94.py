```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.
    Return a balanced (each open brace is properly closed) and not nested within each other
    """
    result = []
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] != '(':
                result.append(char)
                stack = []
        elif stack[-1] == '(':
            stack.append(char)
    else:
                result.append(') ' + stack.pop()
                stack[-1] + char)
    return result
```
This code defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings with each group of parentheses properly separated. The function uses a stack data structure to keep track of open parentheses and closes them as it encounters closing parentheses.
```python
def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []

    for char in paren_string:
        if char == ')':
            if stack:
                result.append(''.join(stack) + char)
                stack.pop()
       
    level = stack and result.stack = []
       for char in stack:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    result.append(''.join(stack) + char)
                    stack.pop()
                else:
                    stack.append(char)

    return result
    ```
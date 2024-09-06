```python
def separate_paren_groups(s: str) -> List[str]:
    result = []
    stack = []

    for char in s:
        if char == ')':
            if stack:
                result.append(''.join(stack) + char)
                stack.pop()
        if char == '(':
                stack.append(char)
            result.append(')

   if char == ' ':
                result.append(''.join(stack) + char)
                stack.pop()
                return result
   ```
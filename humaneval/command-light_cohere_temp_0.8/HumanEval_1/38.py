```python
def separate_paren_groups(s: str) -> List[str]:
    result = []
    stack = []

    for char in s:
        if char == ')':
            if not empty():
                result.append(')'.
                stack.pop()
               
            can open (')
                stack.append(')')
            else:
                    stack.push()
       ')
        stack.append('')
        }
        else:
            if char == '(' and not stack or stack[-1] != ')':
                stack.append(char)
            elif char == ' ' and stack[-1] == '(':
                stack.pop()
            elif char == ' ' and stack[-1] != ')':
                stack.append(' ')
            else:
                stack.push()
                char)
    if len(stack) > 1:
                    result.append(''.pop()
                    result.append(stack.pop())
                []
                    result.append(')')
            return
result

    if not result:
        print("Got empty list")
    return result
```
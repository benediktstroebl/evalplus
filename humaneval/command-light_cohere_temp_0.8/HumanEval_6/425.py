```python
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    for char in parent_string:
        if char == '(':
            stack.append(1)
        else:
            if not stack or char == ')':
                result.append(len)
                stack.append(0)
            elif stack and char == '()':
                result.append(len-1)
                stack.pop()
                elif stack[-1] == int(char):
                    stack.append(1)
                result.append(1)
    return result
```
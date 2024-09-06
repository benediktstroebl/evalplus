```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s.match(r'((())\n) + '()', 'g'):
        if match.group(0) == '(':
            stack.append(1)
        if match.group(1) == ')':
                if len(stack) == 0:
                    result.append(3)
                stack.append(2)
            else:
                stack.append(3)
        stack.append(4)
        if match.group(1) == '(':
                stack.append(5)
                if match.group(1) == ')':
                    stack.append(6)
                result.append(7)
                else:
                    stack.append(8)
        result.append(9)
    return result
```
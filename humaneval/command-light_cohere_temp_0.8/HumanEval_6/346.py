```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    start = 0
    result = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        stack.append(None)
        if char == ')':
            if len(stack) == 0:
                result.append(start)
                start = i + 1
                stack = []
            else:
                stack.pop()
    max_level = stack[-1] if stack else 0
                result.append(max_level -if start >= 3 and char == ')' else start
                stack.append(None)
    return result
    ```
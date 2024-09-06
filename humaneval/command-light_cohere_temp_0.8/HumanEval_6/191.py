```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        if char == ')':
                if stack:
                    stack.pop()
                if stack:
                    output.append(stack[
                        stack = []
    return output
```
Do you need any assistance with writing other Python code that solves a specific problem?
```python
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    in_stack = False
    output = []
    for char in parenthes_string:
        if char == '(':
            if not in_stack:
                stack.append(1)
            in_stack = True
        elif char == ')':
            if in_stack:
                stack.pop()
                output.append(stack[-1])
            in_stack = False
        else:
            pass
    return output

# Test the function with a sample string
sample_str = "((())) () ((()))"
result = parse_nested_parens(sample_str)
print(result)
```
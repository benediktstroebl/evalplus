```python
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []
    for char in parenthes_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                result.append(stack.pop()
               pop the outlined stack to the list result.

test_parse_nested_parens = """
[(()()) ((())) () ((()))]
"""

print(parse_nested_parens(test_parse_nested_parens))
```
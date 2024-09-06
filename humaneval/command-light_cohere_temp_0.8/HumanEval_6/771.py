```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []

    for char in s:
        if char == '(':
            stack.append(0)
        elif char == ')':
            if stack:
                stack.pop()
                if len(stack) == 0:
                    output.append(0)
                else:
                    output.append(stack.pop(). before 2) or thea new level of nesting.

def test_parse_nested_parens(test_string: str) -> None:
    parse_nested_parens(test_string)
```
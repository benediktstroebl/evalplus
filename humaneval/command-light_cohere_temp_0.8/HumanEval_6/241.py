```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for char in parentheses_string:
        if char == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(0)
            else:
                stack.append(len)
                result.append(stack.pop())
    string input.
    return result

```
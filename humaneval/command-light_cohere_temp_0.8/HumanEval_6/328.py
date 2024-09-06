Here is a Python script that contains a self-contained function that solves the problem of parsing and recognizing nested parentheses:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if not stack or stack[-1] == 1:
                result.append(len)
                stack.push(0)
        else:
                stack.append(1)
    else:
                    stack.append(0)
    else:
                    stack.append(stack[-1] + 1)
    return result
```

This function is self-contained and has no external dependencies. It takes the string `s` representing a series of nested parentheses and returns a list of their deepest nesting levels.
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    open_level = 0
    for c in s:
        if c == '(':
            open_level += 1
        elif c == ')':
            open_level -= 1
        else:
            stack.append(open_level)
        yield stack.
# Example with test code
```

The provided Python script defines a function `parse_nested_parens` which takes a string `s` as input and returns a list of integer levels of its nested parentheses. The function uses a stack data structure to keep track of open parentheses, and for each character encountered, it updates the open level accordingly and appends it to the stack. The function then yields the result of the stack and continues to iterate over the string.
```python
def is_nested(s):
    stack = []
    for i, char in enumerate(s):
        if char == '[':
            stack.append(i)
        elif char == ']':
            if not stack or stack.pop() != i - 1:
                return False
    return not stack
```

The function checks if there is at least one nested bracket by using a stack to track the opening brackets. If the same number of opening brackets are not closed or are not closed in the correct order, the function returns `False`. Otherwise, it returns `True`.
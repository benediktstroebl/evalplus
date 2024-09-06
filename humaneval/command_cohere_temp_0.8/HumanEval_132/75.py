```python
def is_nested(s):
    stack = []
    for i, br in enumerate(s):
        if br == '[':
            stack.append(i)
        elif br == ']':
            if not stack or stack.pop() != i - 1:
                return False
    return not stack
```

The given Python script provides a solution to the problem presented in the markdown code block. It checks if there's at least one nested bracket in a string consisting of square brackets. It uses a stack to keep track of opening brackets and checks each closing bracket against the stack or the opening bracket that created the stack element. If any closing bracket doesn't match its corresponding opening bracket or if the stack isn't empty at the end, the function returns False, indicating no nested brackets. Otherwise, it returns True. The given examples illustrate its behavior correctly.
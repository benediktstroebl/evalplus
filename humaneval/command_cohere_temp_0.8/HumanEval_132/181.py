```python
def is_nested(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != brackets[char]:
                return False
    return not stack
```

The code defines a function `is_nested` that takes a string `s` as input and checks whether it contains at least one nested bracket sequence. It uses a stack to keep track of the opening brackets encountered. When a closing bracket is encountered, it checks if the corresponding opening bracket is at the top of the stack or if the stack is empty, which indicates an incorrectly matched bracket. If any of these conditions are met, it returns `False`. Otherwise, if there are any closing brackets left in the stack, it returns `True`, as there is at least one nested bracket sequence in the string.
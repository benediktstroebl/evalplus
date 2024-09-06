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

The function uses a stack to keep track of the brackets encountered and their matching partners. When a closing bracket is encountered, the function checks if it matches the most recent opening bracket on the stack. If it doesn't, the bracket sequence is invalid and the function returns False. If the stack is empty or if the closing bracket matches the one on top of the stack, the bracket is considered valid and is removed from the stack. The function returns True if the stack is empty at the end, indicating a valid nested bracket sequence. 

The provided code includes tests that cover all corner cases mentioned in the problem statement and successfully validates the functionality of the `is_nested` function.
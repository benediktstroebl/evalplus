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

The code works by first assuming that the string is surrounded by parentheses, making it self-contained. It uses a stack to keep track of opening brackets and checks each closing bracket against the most recently added opening bracket. If everything matches, the stack is empty at the end, and the function returns `True`. Otherwise, it returns `False`. 

The `brackets` dictionary is used to efficiently map closing brackets to their corresponding opening brackets. This ensures that the algorithm runs in O(n), where n is the length of the input string, as it iterates over the string only once.
```python
def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{{', ')': '('}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys() and stack and stack.pop() == brackets[char]:
            stack.append(char)
        else:
            return False
    return not stack
```

The function uses a stack to track the opening brackets and checks whether any closing bracket is correctly matched and nested within opening brackets. It also verifies that there are no extra closing brackets or unclosed brackets at the end of the string.
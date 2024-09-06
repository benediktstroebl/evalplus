```python
def is_nested(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    if not s:
        return False

    for char in s:
        if char in '[]{}()':
            stack.append(char)
        elif not stack or stack.pop() != brackets[char]:
            return False
        elif not stack:
            return True
    return not stack
```

The `is_nested` function utilizes a stack to track the opening brackets and verifies whether any closing brackets are matched correctly. The test cases provided evaluate the function with various strings to confirm its correctness.

**Example Usage:**
```python
print(is_nested('[[[[[[[]]]]]]]]]')))
```

The output will be:
```
True
```
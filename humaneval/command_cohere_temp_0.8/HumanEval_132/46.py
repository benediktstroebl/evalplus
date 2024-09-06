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

The following test suite corresponds to the problem statement:
```python
>>> is_nested('[[[[]]])
True

>>> is_nested('[][]')
False

>>> is_nested('[]')
False

>>> is_nested('([[])')
True

>>> is_nested('([([])')
False

>>> is_nested('[[[[[(()
False
```
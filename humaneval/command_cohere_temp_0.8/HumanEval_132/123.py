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

The following code uses a stack to solve the problem:
1. It iterates through each character in the string `s`.
2. If the character is an open bracket: `('(``, ` '[``, ` '{'`)`, it pushes it onto the stack.
3. If the character is a closing bracket: `')'`, `']'`, `'}'`, it checks if the stack is empty or if the top of the stack is different from the expected opening bracket. If either condition is True, it returns `False` since a closing bracket has been encountered that isn't properly matched. Otherwise, it pops the top bracket from the stack, and if the stack becomes empty, it returns `True`, as a properly matched bracket sequence has been found.

The script handles several edge cases correctly, including scenarios with different bracket quantities and misplaced brackets.

The code has a time complexity of O(n), where n is the number of characters in the string, and a space complexity of O(1) as it only uses a single list to keep track of open brackets.
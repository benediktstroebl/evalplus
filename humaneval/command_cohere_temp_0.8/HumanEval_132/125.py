```python
def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{{', ')': '('}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            top = stack.pop() if stack else '#'
            if brackets[top] != brackets[char]:
                return False
        else:
            continue

    return not stack
```

The following code uses a stack to keep track of the brackets and iterates over the characters in the input string. When a closing bracket is encountered, it is pushed to the stack. When an opening bracket is encountered, the top bracket from the stack is checked to see if it matches the required opening bracket. If it does not, the sequence is not nested and the function returns False. If it does match, the bracket is popped from the stack to simulate closing the previous bracket pair.

The function returns True if there are no unmatched brackets left in the stack at the end of the string, indicating a nested sequence of brackets.

To ensure that the code handles all corner cases, several test cases are provided in the problem statement.
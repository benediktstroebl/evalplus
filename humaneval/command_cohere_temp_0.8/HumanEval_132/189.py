```python
def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{', ')': '('}

    for char in s:
        if char in '][}:':
            stack.append(char)
        elif char in '[({':
            if not stack or stack.pop() != brackets[char]:
                return False
        else:
            # Ignore non-bracket characters
            continue

    return not stack
```

The following code uses a stack to track the opening brackets encountered while iterating over the input string. When a closing bracket is encountered, it is checked against the top of the stack. If they do not match or if the stack is empty, then the sequence is not nested. If the stack is not empty at the end of the loop, it means there is a missing closing bracket, indicating a nested sequence. 

To run the code, you can copy and paste it into a Python environment of your choice and run the `is_nested()` function with the input strings provided in the original problem statement to see the results. 

Please let me know if this code correctly resolves the problem statement or if you'd like me to explain any part of the code in more detail.
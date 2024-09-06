```python
def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{', ']': '['}

    for bracket in s:
        if bracket in brackets.values():
            stack.append(bracket)
        else:
            try:
                top_bracket = stack.pop()
            except IndexError:
                return False
            if top_bracket != brackets[bracket]:
                return False
    return not stack
```

The provided Python code defines a function called `is_nested` that checks whether a given string contains at least one nested pair of square brackets. The function uses a stack to keep track of the square brackets encountered while iterating through the input string. It also utilizes a dictionary called `brackets` to map opening brackets to their corresponding closing brackets.

When the function encounters an opening bracket, it pushes it onto the stack. When a closing bracket is encountered, the function checks if it matches the most recent opening bracket on the stack. If not, the function returns `False` as the input string contains an invalid sequence of brackets. If the closing bracket matches the top bracket on the stack, it is removed from the stack.

If the stack is empty and no valid nested brackets are found, the function returns `True`. Otherwise, it returns `False`.

This code demonstrates an efficient way to check for nested brackets in a string, avoiding unnecessary checks and ensuring a linear time complexity.
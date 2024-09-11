```python
def correct_bracketing(brackets: str):
    """brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack:
                return False
            else:
                stack.pop()
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script works by using a stack to keep track of the opening brackets encountered so far. When it encounters a closing bracket, it checks if the stack is empty (i.e., there's no corresponding opening bracket) and returns False if so. If the stack is not empty, it pops the opening bracket from the stack. After iterating over all brackets, it returns True if the stack is empty (i.e., every opening bracket has been matched) and False otherwise.
```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket in a string has a corresponding closing bracket.

    Args:
    brackets (str): A string consisting of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack to store opening brackets
    for bracket in brackets:
        if bracket == "<":  # If the current bracket is an opening bracket, push it onto the stack
            stack.append(bracket)
        elif bracket == ">":  # If the current bracket is a closing bracket
            if not stack:  # If the stack is empty, it means there's no corresponding opening bracket
                return False
            stack.pop()  # If the stack is not empty, pop the top opening bracket off the stack
    return not stack  # After iterating over the entire string, if the stack is empty, it means every opening bracket had a corresponding closing bracket

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines a function `correct_bracketing` that takes a string of "<" and ">" as input. It uses a stack to keep track of the opening brackets in the string. For each closing bracket it encounters, it checks if the stack is empty. If it is, it returns `False` because there's no corresponding opening bracket for the current closing bracket. If the stack is not empty, it pops the top opening bracket off the stack. After iterating over the entire string, it checks if the stack is empty. If it is, it returns `True` because every opening bracket had a corresponding closing bracket. If the stack is not empty, it returns `False` because there are some opening brackets that don't have corresponding closing brackets.
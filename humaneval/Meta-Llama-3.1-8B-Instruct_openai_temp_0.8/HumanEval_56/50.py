```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if a string of "<" and ">" has correct bracketing.

    Args:
    brackets (str): A string consisting of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the character is a closing bracket and the stack is empty, return False
        elif bracket == ">" and not stack:
            return False
        # If the character is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ">":
            stack.pop()

    # If the stack is empty after iterating over the entire string, return True
    # Otherwise, return False because there are unmatched opening brackets
    return not stack


# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines a function `correct_bracketing` that uses a stack to keep track of the opening brackets. It iterates over each character in the input string, pushing opening brackets onto the stack and popping them off when it encounters a closing bracket. If it encounters a closing bracket when the stack is empty, it returns `False`. After iterating over the entire string, it returns `True` if the stack is empty (meaning all opening brackets were matched) and `False` otherwise.
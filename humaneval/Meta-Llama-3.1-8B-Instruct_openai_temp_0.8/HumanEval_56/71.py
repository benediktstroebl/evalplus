```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: Whether the brackets are correctly paired.
    """
    stack = []  # Initialize an empty stack

    for bracket in brackets:
        # If the bracket is an opening bracket, push it to the stack
        if bracket == "<":
            stack.append(bracket)
        # If the bracket is a closing bracket and the stack is not empty
        elif bracket == ">" and stack:
            # Pop the opening bracket from the stack
            stack.pop()

    # If the stack is empty, all opening brackets have a corresponding closing bracket
    return not stack


# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script uses a stack to keep track of the opening brackets. It iterates over the string, pushing opening brackets onto the stack and popping them when it encounters a corresponding closing bracket. If the stack is empty at the end, all opening brackets have been closed correctly.
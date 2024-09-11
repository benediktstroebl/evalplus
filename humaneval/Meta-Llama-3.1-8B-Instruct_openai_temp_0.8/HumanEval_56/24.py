```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket has a corresponding closing bracket in the given string.

    Args:
        brackets (str): A string consisting of "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a stack to keep track of opening brackets
    stack = []

    # Iterate over the input string
    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the bracket is a closing bracket
        elif bracket == ">":
            # If the stack is empty, there's no corresponding opening bracket
            if not stack:
                return False
            # Otherwise, pop the opening bracket from the stack
            else:
                stack.pop()

    # If the stack is empty after iterating over the entire string, every opening bracket has a corresponding closing bracket
    return not stack


# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```
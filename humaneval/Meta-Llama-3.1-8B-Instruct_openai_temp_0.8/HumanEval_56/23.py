```python
def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack

    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the bracket is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ">" and stack:
            stack.pop()
        # If the bracket is a closing bracket and the stack is empty, return False
        elif bracket == ">":
            return False

    # If the stack is empty after processing all brackets, return True
    # If the stack is not empty, it means there are unmatched opening brackets, so return False
    return not stack


# Test cases
print(correct_bracketing("<"))     # False
print(correct_bracketing("<>"))    # True
print(correct_bracketing("<<><>>")) # True
print(correct_bracketing("><<><>")) # False
```
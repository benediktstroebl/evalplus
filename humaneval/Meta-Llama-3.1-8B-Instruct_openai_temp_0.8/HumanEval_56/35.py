```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack to store opening brackets
    for bracket in brackets:
        if bracket == "<":  # If the current character is an opening bracket
            stack.append(bracket)  # Push it onto the stack
        elif bracket == ">":  # If the current character is a closing bracket
            if not stack:  # If the stack is empty (i.e., there's no corresponding opening bracket)
                return False  # Return False
            stack.pop()  # Otherwise, pop the corresponding opening bracket from the stack
    return not stack  # If the stack is empty after checking all brackets, return True; otherwise, return False

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```
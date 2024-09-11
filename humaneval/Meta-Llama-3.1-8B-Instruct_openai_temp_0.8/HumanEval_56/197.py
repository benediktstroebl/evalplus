```python
def correct_bracketing(brackets: str) -> bool:
    """Returns True if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the bracket is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ">" and stack:
            stack.pop()
    # If the stack is empty after processing the entire string, it means every opening bracket has a corresponding closing bracket
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```
```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket has a corresponding closing bracket in the given string.

    Args:
        brackets (str): A string consisting of "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack
    for bracket in brackets:
        # If we encounter an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If we encounter a closing bracket, check if the stack is empty or the top of the stack does not match
        elif bracket == ">":
            if not stack or stack.pop()!= "<":
                return False  # If the stack is empty or the top of the stack does not match, return False
    # After checking all brackets, return True if the stack is empty (i.e., every opening bracket had a corresponding closing bracket)
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```
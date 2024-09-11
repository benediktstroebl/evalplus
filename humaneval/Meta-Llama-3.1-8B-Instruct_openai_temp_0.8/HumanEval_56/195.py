```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">", where "<" represents an opening bracket and ">" represents a closing bracket.

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack to keep track of the opening brackets

    for bracket in brackets:
        if bracket == "<":  # If the current bracket is an opening bracket
            stack.append(bracket)  # Push it onto the stack
        elif bracket == ">":  # If the current bracket is a closing bracket
            if not stack:  # If the stack is empty
                return False  # Return False because there's no corresponding opening bracket
            stack.pop()  # Pop the corresponding opening bracket from the stack

    return not stack  # After processing all brackets, return True if the stack is empty (i.e., all opening brackets have corresponding closing brackets)


# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```
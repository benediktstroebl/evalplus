```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: Whether every opening bracket has a corresponding closing bracket.
    """
    # Initialize a stack to store the opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the character is a closing bracket
        elif bracket == ">":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # Otherwise, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # If the stack is empty after iterating over the entire string, every opening bracket had a corresponding closing bracket, so return True
    # Otherwise, there were unmatched opening brackets, so return False
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script uses a stack to keep track of the opening brackets. It pushes opening brackets onto the stack and pops them off when it encounters a corresponding closing bracket. If it encounters a closing bracket when the stack is empty, it returns False, because there's no corresponding opening bracket. Finally, it checks if the stack is empty after iterating over the entire string. If it is, every opening bracket had a corresponding closing bracket, so it returns True. Otherwise, there were unmatched opening brackets, so it returns False.
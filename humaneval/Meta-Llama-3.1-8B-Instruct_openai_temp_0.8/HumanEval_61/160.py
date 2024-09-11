```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if a string of '(' and ')' has correct bracketing.

    Args:
        brackets (str): A string of '(' and ')'.

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a stack to store opening brackets
    stack = []

    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the character is a closing bracket, check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()

    # After iterating over the entire string, if the stack is empty, every opening bracket has a corresponding closing bracket
    return not stack


# Test cases
if not correct_bracketing("("):
    pass
if correct_bracketing("()"):
    pass
if correct_bracketing("(()())"):
    pass
if not correct_bracketing(")(()"):
    pass
```

This script uses a stack data structure to keep track of opening brackets. It iterates over each character in the string, pushing opening brackets onto the stack and popping them off when it encounters a closing bracket. If it encounters a closing bracket when the stack is empty, or if there are any opening brackets left in the stack after iterating over the entire string, it returns False, indicating incorrect bracketing. Otherwise, it returns True, indicating correct bracketing.
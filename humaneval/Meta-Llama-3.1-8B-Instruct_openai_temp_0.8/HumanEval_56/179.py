```python
def correct_bracketing(brackets: str):
    """
    Checks if a string of "<" and ">" has correct bracketing.
    
    Args:
    brackets (str): A string consisting of "<" and ">".
    
    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    
    # Iterate over the string
    for bracket in brackets:
        # If the bracket is an opening bracket, push it to the stack
        if bracket == "<":
            stack.append(bracket)
        # If the bracket is a closing bracket and the stack is not empty, pop the stack
        elif bracket == ">" and stack:
            stack.pop()
        # If the bracket is a closing bracket but the stack is empty, return False
        elif bracket == ">":
            return False
    
    # If the stack is empty after iterating over the string, return True
    # Otherwise, return False (because there are unmatched opening brackets)
    return not stack


# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script uses a stack data structure to keep track of the opening brackets. It iterates over the string, pushing opening brackets onto the stack and popping them when it encounters a closing bracket. If it encounters a closing bracket when the stack is empty, it returns False. After iterating over the string, it returns True if the stack is empty (meaning all opening brackets have been matched) and False otherwise.
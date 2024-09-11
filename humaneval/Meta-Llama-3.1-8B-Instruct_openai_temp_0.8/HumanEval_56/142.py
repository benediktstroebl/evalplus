```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if a string of "<" and ">" contains matching opening and closing brackets.

    Args:
    brackets (str): A string consisting of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        # If we encounter an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If we encounter a closing bracket, check if the stack is empty
        elif bracket == ">":
            if not stack:
                # If the stack is empty, there's no matching opening bracket, so return False
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            stack.pop()
    
    # After iterating through the entire string, if the stack is empty, it means every opening bracket had a corresponding closing bracket
    return not stack


# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script uses a stack to keep track of the opening brackets. It iterates through the input string, pushing opening brackets onto the stack and popping them when it encounters a closing bracket. If it encounters a closing bracket when the stack is empty, it returns False, because there's no matching opening bracket. Finally, it checks if the stack is empty after iterating through the entire string. If the stack is empty, it means every opening bracket had a corresponding closing bracket, so it returns True. Otherwise, it returns False.
```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the given string has a corresponding closing bracket.

    Args:
    brackets (str): A string consisting of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Initialize a stack to store the opening brackets
    stack = []
    
    # Iterate over the string
    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the bracket is a closing bracket
        elif bracket == ">":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the string, if the stack is empty, it means every opening bracket had a corresponding closing bracket
    # So return True
    # If the stack is not empty, it means there were some opening brackets without corresponding closing brackets, so return False
    return not stack


# Example usage:
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines the `correct_bracketing` function, which uses a stack to check if every opening bracket in the given string has a corresponding closing bracket. The function returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. The example usage at the end demonstrates how to use this function with different inputs.
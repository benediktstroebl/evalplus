```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Create a stack to store the opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the bracket is a closing bracket, check if the stack is empty
        elif bracket == ">":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, if the stack is empty, every opening bracket has a corresponding closing bracket
    # So return True
    if not stack:
        return True
    # If the stack is not empty, there are some opening brackets without corresponding closing brackets, so return False
    else:
        return False

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines a function `correct_bracketing` that takes a string of "<" and ">" as input and returns True if every opening bracket has a corresponding closing bracket, and False otherwise. It uses a stack to keep track of the opening brackets and checks if the stack is empty after iterating over the entire string. The test cases are included at the end to demonstrate the function's behavior.
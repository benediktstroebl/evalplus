```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.
    
    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: Whether every opening bracket has a corresponding closing bracket.
    """
    # Initialize a stack to keep track of opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the character is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ">" and stack:
            stack.pop()
    
    # If the stack is empty after iterating over the entire string, every opening bracket has a corresponding closing bracket
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines a function called `correct_bracketing` that takes a string of "<" and ">" as input and returns `True` if every opening bracket has a corresponding closing bracket, and `False` otherwise. The function uses a stack to keep track of the opening brackets it encounters, and checks if the stack is empty at the end to determine if every opening bracket has a corresponding closing bracket.
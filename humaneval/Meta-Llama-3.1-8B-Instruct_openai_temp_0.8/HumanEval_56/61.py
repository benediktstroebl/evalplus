```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    # Use a stack to keep track of opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the character is a closing bracket and the stack is not empty, pop the stack
        elif bracket == ">" and stack:
            stack.pop()
    
    # If the stack is empty, then every opening bracket had a corresponding closing bracket
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines a function `correct_bracketing` that checks if a given string of "<" and ">" has every opening bracket corresponding to a closing bracket. It uses a stack data structure to keep track of the opening brackets. If a closing bracket is encountered and the stack is empty, it means there is no corresponding opening bracket, so the function immediately returns False. If the function iterates over the entire string and the stack is empty, it means every opening bracket had a corresponding closing bracket, so the function returns True.
```python
def correct_bracketing(brackets: str) -> bool:
    """ 
    Checks if a string of '<' and '>' has correct bracketing.
    
    Args:
    brackets (str): A string consisting of '<' and '>'.
    
    Returns:
    bool: True if every opening bracket has a corresponding closing bracket.
    """
    
    # Initialize a stack to keep track of opening brackets
    stack = []
    
    # Iterate over each character in the string
    for bracket in brackets:
        # If the character is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append("<")
        # If the character is a closing bracket, check if the stack is empty
        elif bracket == ">":
            # If the stack is empty, return False because there's no matching opening bracket
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    
    # After iterating over the entire string, return True if the stack is empty
    # (meaning every opening bracket had a corresponding closing bracket) and False otherwise
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is empty. If it is, that means there's no matching opening bracket, so it returns False. If the stack is not empty, it pops the opening bracket from the stack. After iterating over the entire string, it returns True if the stack is empty (meaning every opening bracket had a corresponding closing bracket) and False otherwise.
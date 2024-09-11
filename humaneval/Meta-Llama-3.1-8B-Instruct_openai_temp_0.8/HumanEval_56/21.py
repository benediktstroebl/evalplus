```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: Whether the brackets are correctly paired.
    """
    stack = []
    
    # Push opening brackets onto the stack
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        # Pop the stack when a closing bracket is encountered
        elif bracket == ">":
            if not stack:
                return False  # Unbalanced brackets
            stack.pop()
    
    # If the stack is empty, then brackets were correctly paired
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

In this script, we use a stack data structure to keep track of the opening brackets. When a closing bracket is encountered, we check if the stack is empty. If it is, that means there's no corresponding opening bracket, so we return False. If the stack is not empty, we pop the top element from the stack. Finally, if the stack is empty after processing all the brackets, we return True, indicating that the brackets were correctly paired.
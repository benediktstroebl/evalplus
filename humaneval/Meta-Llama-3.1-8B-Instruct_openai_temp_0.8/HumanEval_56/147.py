```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: Whether every opening bracket has a corresponding closing bracket.
    """
    stack = []
    for bracket in brackets:
        # If we encounter an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If we encounter a closing bracket, check if the stack is empty
        elif bracket == ">":
            # If the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    # After iterating over all brackets, if the stack is empty, it means every opening bracket had a corresponding closing bracket, so return True
    # If the stack is not empty, it means there were some opening brackets without corresponding closing brackets, so return False
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script defines a function `correct_bracketing` that takes a string of "<" and ">" as input and returns a boolean value indicating whether every opening bracket has a corresponding closing bracket. The function uses a stack to keep track of the opening brackets. If we encounter an opening bracket, we push it onto the stack. If we encounter a closing bracket, we check if the stack is empty. If it's empty, there's no corresponding opening bracket, so we return False. If the stack is not empty, we pop the opening bracket from the stack. After iterating over all brackets, we check if the stack is empty. If it is, every opening bracket had a corresponding closing bracket, so we return True. If the stack is not empty, there were some opening brackets without corresponding closing brackets, so we return False.
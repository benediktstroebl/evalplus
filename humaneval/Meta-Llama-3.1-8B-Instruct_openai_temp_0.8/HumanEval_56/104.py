```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket in a string has a corresponding closing bracket.

    Args:
        brackets (str): A string consisting of "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if stack:
                stack.pop()
            else:
                return False
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

This script uses a stack data structure to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is not empty; if it's not empty, it pops the top element off the stack (which represents the corresponding opening bracket). If the stack is empty or the stack is not empty but the top element is not an opening bracket, it returns False. Finally, it checks if the stack is empty at the end; if it's not empty, it means there are some opening brackets without corresponding closing brackets, and it returns False. If the stack is empty, it returns True.
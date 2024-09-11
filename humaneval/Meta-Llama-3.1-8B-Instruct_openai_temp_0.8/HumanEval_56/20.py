```python
def correct_bracketing(brackets: str):
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack:
                return False
            stack.pop()
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
```

In this script, we use a stack data structure to keep track of the opening brackets we encounter. When we encounter a closing bracket, we check if the stack is empty. If it is, that means there's no corresponding opening bracket, so we return False. If the stack is not empty, we pop the opening bracket from the stack. After going through all the brackets, we check if the stack is empty. If it is, that means every opening bracket has a corresponding closing bracket, so we return True. If the stack is not empty, that means there are some opening brackets without corresponding closing brackets, so we return False.
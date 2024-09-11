```python
def correct_bracketing(brackets: str):
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">".

    Returns:
        bool: Whether every opening bracket has a corresponding closing bracket.
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
if not correct_bracketing("<"):
    print("Test case 1 passed")
if correct_bracketing("<>"):
    print("Test case 2 passed")
if correct_bracketing("<<><>>"):
    print("Test case 3 passed")
if not correct_bracketing("><<>"):
    print("Test case 4 passed")
```

This script uses a stack to keep track of the opening brackets. It iterates over the string of brackets, pushing "<" onto the stack and popping "<" from the stack when it encounters ">". If it encounters ">" when the stack is empty, it immediately returns False, indicating that there is no corresponding opening bracket for the closing bracket. After iterating over the entire string, it returns whether the stack is empty. If the stack is empty, that means every opening bracket has a corresponding closing bracket, so it returns True. Otherwise, it returns False.
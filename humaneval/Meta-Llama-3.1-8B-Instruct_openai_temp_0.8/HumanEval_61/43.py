```python
def correct_bracketing(brackets: str):
    """brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack:
                return False
            stack.pop()
    return not stack


# Test the function
if not correct_bracketing("("):
    print("Test case 1 passed")
if correct_bracketing("()"):
    print("Test case 2 passed")
if correct_bracketing("(()())"):
    print("Test case 3 passed")
if not correct_bracketing(")(()"):
    print("Test case 4 passed")
```
This script uses a stack to keep track of the opening brackets encountered so far. When it encounters a closing bracket, it checks if the stack is empty, which would mean there's no corresponding opening bracket. If the stack is not empty, it pops the opening bracket from the stack. At the end, it checks if the stack is empty. If it is, that means every opening bracket has a corresponding closing bracket, and it returns `True`. If not, it returns `False`.
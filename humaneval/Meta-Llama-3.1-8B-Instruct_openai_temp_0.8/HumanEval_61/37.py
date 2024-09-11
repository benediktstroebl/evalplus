```python
def correct_bracketing(brackets: str):
    """
    checks if every opening bracket has a corresponding closing bracket

    Args:
        brackets (str): a string of "(" and ")"

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise
    """
    stack = []  # initialize an empty stack

    for bracket in brackets:
        if bracket == "(":  # if the current bracket is an opening bracket
            stack.append(bracket)  # push it onto the stack
        elif bracket == ")":  # if the current bracket is a closing bracket
            if not stack:  # if the stack is empty
                return False  # there's no matching opening bracket, so return False
            stack.pop()  # remove the matching opening bracket from the stack

    return not stack  # if the stack is empty after processing all brackets, return True; otherwise, return False


# test cases
if correct_bracketing("("):
    assert False, "Test case failed: () should return False"

if correct_bracketing("()"):
    assert True

if correct_bracketing("(()())"):
    assert True

if not correct_bracketing(")(()"):
    assert True
```

This script defines a function `correct_bracketing` that uses a stack to check if every opening bracket has a corresponding closing bracket. It iterates over the input string, pushing opening brackets onto the stack and popping them when a closing bracket is encountered. If the stack is empty after processing all brackets, it means every opening bracket had a corresponding closing bracket, and the function returns `True`. Otherwise, it returns `False`. The test cases at the end verify the function's correctness.
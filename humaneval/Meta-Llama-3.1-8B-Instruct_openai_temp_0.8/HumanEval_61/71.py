```python
def correct_bracketing(brackets: str) -> bool:
    """
    checks if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): a string of "(" and ")"

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise
    """
    # use a stack to keep track of opening brackets
    stack = []

    # iterate over the string
    for bracket in brackets:
        # if the bracket is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # if the bracket is a closing bracket, check if the stack is empty
        elif bracket == ")":
            # if the stack is empty, there's no corresponding opening bracket, so return False
            if not stack:
                return False
            # if the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()

    # after iterating over the string, if the stack is empty, every opening bracket had a corresponding closing bracket, so return True
    # if the stack is not empty, there's at least one opening bracket without a corresponding closing bracket, so return False
    return not stack


# test the function
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()}"))  # False
print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that uses a stack to check if every opening bracket has a corresponding closing bracket. It then tests this function with some example inputs.
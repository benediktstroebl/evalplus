```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the given string has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack

    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the bracket is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ")" and stack:
            stack.pop()
        # If the bracket is a closing bracket and the stack is empty, return False because there's no corresponding opening bracket
        elif bracket == ")":
            return False

    # If the stack is empty after iterating over all brackets, return True; otherwise, return False
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that uses a stack to track the opening brackets in the input string. It then checks if every opening bracket has a corresponding closing bracket. The function returns `True` if every opening bracket has a corresponding closing bracket and `False` otherwise. The test cases at the end of the script demonstrate the function's behavior.
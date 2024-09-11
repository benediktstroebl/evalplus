```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        # If the bracket is an opening bracket, push it to the stack
        if bracket == "(":
            stack.append(bracket)
        # If the bracket is a closing bracket and the stack is not empty, pop the opening bracket from the stack
        elif bracket == ")" and stack:
            stack.pop()
        # If the bracket is a closing bracket and the stack is empty, return False
        elif bracket == ")":
            return False
    # If the stack is empty after iterating over all brackets, return True
    # If the stack is not empty, return False because there are unmatched opening brackets
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that uses a stack data structure to keep track of the opening brackets. It iterates over the string, pushing opening brackets to the stack and popping them when it encounters a closing bracket. If it encounters a closing bracket when the stack is empty, or if the stack is not empty after iterating over all brackets, it returns False. Otherwise, it returns True.
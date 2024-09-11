```python
def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket in the string has a corresponding closing bracket.

    Args:
    brackets (str): A string containing only "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            # Push "(" onto the stack
            stack.append(bracket)
        elif bracket == ")":
            # If the stack is empty or the top of the stack is not "(", return False
            if not stack or stack.pop()!= "(":
                return False
    # If the stack is empty after processing all brackets, return True
    # Otherwise, return False because there are unmatched "("
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script defines a function `correct_bracketing` that uses a stack to keep track of the opening brackets encountered so far. When it encounters a closing bracket, it checks if the top of the stack is an opening bracket. If it is, it pops the opening bracket from the stack. If the stack is empty or the top of the stack is not an opening bracket, it immediately returns `False`. After processing all the brackets, it returns `True` if the stack is empty (meaning every opening bracket has a corresponding closing bracket) and `False` otherwise (meaning there are unmatched opening brackets).
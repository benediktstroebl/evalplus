```python
def correct_bracketing(brackets: str):
    """
    Returns True if every opening bracket in the string has a corresponding closing bracket.

    Args:
        brackets (str): A string consisting of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []  # Initialize an empty stack

    for bracket in brackets:
        if bracket == "(":  # If the current bracket is an opening bracket
            stack.append(bracket)  # Push it to the stack
        elif bracket == ")":  # If the current bracket is a closing bracket
            if not stack:  # If the stack is empty (no matching opening bracket)
                return False  # Return False
            stack.pop()  # Pop the matching opening bracket from the stack

    return not stack  # Return True if every opening bracket has a corresponding closing bracket, False otherwise


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script uses a stack to keep track of the opening brackets encountered in the string. When a closing bracket is encountered, it checks if there's a matching opening bracket on the stack. If not, it immediately returns `False`. If the stack is empty when a closing bracket is encountered, it also returns `False`. Finally, it returns `True` if the stack is empty after processing the entire string (meaning every opening bracket has been matched with a closing bracket), and `False` otherwise.
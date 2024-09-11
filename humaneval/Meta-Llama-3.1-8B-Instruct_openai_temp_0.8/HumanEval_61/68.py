```python
def correct_bracketing(brackets: str):
    """
    Checks if a string of parentheses has correct bracketing.

    Args:
        brackets (str): A string of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            # Push opening bracket to the stack
            stack.append(bracket)
        elif bracket == ")":
            # If stack is empty, there's no corresponding opening bracket
            if not stack:
                return False
            # Pop opening bracket from the stack
            stack.pop()
    # If stack is empty after processing all brackets, every opening bracket has a corresponding closing bracket
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(("))  # False
print(correct_bracketing("((()()))")) # True
print(correct_bracketing(")()("))  # False
```
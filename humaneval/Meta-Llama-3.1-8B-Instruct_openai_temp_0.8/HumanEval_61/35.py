### Correct Bracketing Function
```python
def correct_bracketing(brackets: str):
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
            stack.append(bracket)
        elif bracket == ")":
            if len(stack) == 0:
                # If the stack is empty, there is no corresponding opening bracket
                return False
            stack.pop()
    # If the stack is empty after checking all brackets, every opening bracket has a corresponding closing bracket
    return len(stack) == 0

# Test cases
print(correct_bracketing("("))    # False
print(correct_bracketing("()"))    # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```
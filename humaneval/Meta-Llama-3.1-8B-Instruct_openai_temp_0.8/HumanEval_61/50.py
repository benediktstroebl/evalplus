```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket in a string has a corresponding closing bracket.

    Args:
        brackets (str): A string of "(" and ")".

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack:
                return False  # No corresponding opening bracket
            stack.pop()
    return not stack  # If stack is empty, all brackets were matched


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()}"))  # False
print(correct_bracketing(")(()"))  # False
print(correct_bracketing(""))  # True
print(correct_bracketing("(" * 100 + ")" * 100))  # True
```
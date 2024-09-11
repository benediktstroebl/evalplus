```python
def correct_bracketing(brackets: str):
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            # Push opening bracket onto the stack
            stack.append(bracket)
        elif bracket == ")":
            # If the stack is empty, there's no matching opening bracket
            if not stack:
                return False
            # Pop the opening bracket from the stack
            stack.pop()
    # If the stack is empty, every opening bracket has a matching closing bracket
    return not stack

# Test cases
print(correct_bracketing("("))  # Should print: False
print(correct_bracketing("()"))  # Should print: True
print(correct_bracketing("(()())"))  # Should print: True
print(correct_bracketing(")(()"))  # Should print: False
```
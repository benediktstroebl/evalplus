```python
def correct_bracketing(brackets: str):
    """
    Checks if a string of brackets has correct pairing.

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
            # If there are no opening brackets to pop, or if the top of the stack doesn't match the closing bracket, return False
            if not stack or (stack[-1]!= "("):
                return False
            # Pop the opening bracket from the stack
            stack.pop()
    # If the stack is empty after processing all brackets, then every opening bracket has a corresponding closing bracket
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script uses a stack to keep track of the opening brackets encountered so far. When a closing bracket is encountered, it checks if the top of the stack contains an opening bracket that matches it. If not, it returns False. After processing all brackets, it checks if the stack is empty. If it is, then every opening bracket has a corresponding closing bracket, and it returns True. Otherwise, it returns False.
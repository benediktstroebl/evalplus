```python
def correct_bracketing(brackets: str):
    """Check if every opening bracket has a corresponding closing bracket.

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
                return False
            stack.pop()
    return not stack

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script uses a stack data structure to keep track of the opening brackets. When a closing bracket is encountered, it checks if the stack is empty. If it is, it means there's no corresponding opening bracket, so it returns False. If the stack is not empty, it pops the opening bracket from the stack. After checking all brackets, it returns True if the stack is empty (meaning every opening bracket had a corresponding closing bracket) and False otherwise.
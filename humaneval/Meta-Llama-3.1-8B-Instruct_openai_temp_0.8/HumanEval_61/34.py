```python
def correct_bracketing(brackets: str):
    """
    Check if every opening bracket has a corresponding closing bracket.

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
print(correct_bracketing("(")) # False
print(correct_bracketing("()")) # True
print(correct_bracketing("(()())")) # True
print(correct_bracketing(")(()")) # False
```

This script defines a function `correct_bracketing` that uses a stack to keep track of the opening brackets. For each opening bracket encountered, it pushes it onto the stack. For each closing bracket encountered, it checks if the stack is empty (in which case it immediately returns False, because there's no corresponding opening bracket) and if not, it pops the opening bracket from the stack. Finally, it checks if the stack is empty after processing all brackets. If it is, it means every opening bracket had a corresponding closing bracket, so it returns True. Otherwise, it returns False.
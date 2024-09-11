```python
def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "(" and ")".

    Returns:
    bool: True if the brackets are correctly paired, False otherwise.
    """
    stack = []
    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "(":
            stack.append(bracket)
        # If the bracket is a closing bracket, check if the stack is empty
        elif bracket == ")":
            # If the stack is empty, return False because there's no matching opening bracket
            if not stack:
                return False
            # If the stack is not empty, pop the opening bracket from the stack
            else:
                stack.pop()
    # After iterating over all brackets, if the stack is empty, return True
    # Because every opening bracket has been matched with a closing bracket
    # If the stack is not empty, return False because there are unmatched opening brackets
    return not stack


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This script uses a stack data structure to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is empty. If it is, it means there's no matching opening bracket, so it returns False. If the stack is not empty, it pops the opening bracket from the stack. After iterating over all brackets, it checks if the stack is empty. If it is, it means every opening bracket has been matched with a closing bracket, so it returns True. If the stack is not empty, it means there are unmatched opening brackets, so it returns False.
```python
def correct_bracketing(brackets: str):
    """Returns True if every opening bracket has a corresponding closing bracket.

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

This script uses a stack data structure to keep track of the opening brackets. When a closing bracket is encountered, it checks if the stack is empty. If it is, that means there's no corresponding opening bracket, so the function returns False. If the stack is not empty, it pops the opening bracket from the stack. After processing all the brackets, the function checks if the stack is empty. If it is, that means every opening bracket has a corresponding closing bracket, so the function returns True. If the stack is not empty, that means there are some opening brackets without corresponding closing brackets, so the function returns False.
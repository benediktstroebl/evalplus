```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket has a corresponding closing bracket.

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
            if not stack:  # if the stack is empty, there's no corresponding opening bracket
                return False
            stack.pop()
    return not stack  # if the stack is empty after checking all brackets, every opening bracket has a corresponding closing bracket


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
print(correct_bracketing("()()()"))  # True
print(correct_bracketing("(" * 100 + ")" * 99))  # False
```

This script uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is empty (i.e., there's no corresponding opening bracket). If the stack is not empty, it pops the opening bracket from the stack. After checking all brackets, it returns True if the stack is empty (i.e., every opening bracket has a corresponding closing bracket) and False otherwise.
```python
def correct_bracketing(brackets: str):
    """
    brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.
    
    :param brackets: A string of "(" and ")".
    :return: True if every opening bracket has a corresponding closing bracket.
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

This script defines a function `correct_bracketing` that checks if every opening bracket has a corresponding closing bracket in the given string. It uses a stack to keep track of the opening brackets. If it encounters a closing bracket and the stack is empty, it returns False. If it encounters a closing bracket and the stack is not empty, it pops the opening bracket from the stack. At the end, it returns True if the stack is empty (which means every opening bracket has been closed) and False otherwise.
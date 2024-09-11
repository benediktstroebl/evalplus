```python
def correct_bracketing(brackets: str):
    """brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
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

This script uses a stack data structure to track the opening brackets. It iterates over the input string, pushing opening brackets onto the stack and popping them off when it encounters a closing bracket. If it encounters a closing bracket when the stack is empty, it immediately returns `False`. After iterating over the entire string, it returns `True` if the stack is empty (meaning every opening bracket was closed) and `False` otherwise.
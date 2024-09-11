```python
def correct_bracketing(brackets: str) -> bool:
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
                return False  # Unmatched closing bracket
            stack.pop()
    return not stack  # If stack is empty, all brackets were matched


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(("))  # False
print(correct_bracketing("(" * 100 + ")" * 100))  # True
print(correct_bracketing("(" * 100 + ")" * 101))  # False
```
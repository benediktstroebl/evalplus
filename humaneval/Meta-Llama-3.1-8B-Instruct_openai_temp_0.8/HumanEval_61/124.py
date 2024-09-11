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
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(("))  # False
```

This script uses a stack data structure to check if every opening bracket has a corresponding closing bracket. When an opening bracket is encountered, it is pushed onto the stack. When a closing bracket is encountered, it is checked if the stack is empty (which means there is no corresponding opening bracket) or if it is popped from the stack (which means the corresponding opening bracket has been found). After checking all brackets, the script returns whether the stack is empty, which means every opening bracket has been matched with a closing bracket.
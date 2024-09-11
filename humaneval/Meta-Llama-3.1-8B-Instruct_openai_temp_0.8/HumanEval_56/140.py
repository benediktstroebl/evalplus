```python
def correct_bracketing(brackets: str):
    """brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack:
                return False
            stack.pop()
    return not stack

# Test cases
print(correct_bracketing("<"))       # False
print(correct_bracketing("<>"))      # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))    # False
```

In this script, a stack is used to keep track of the opening brackets. When an opening bracket is encountered, it is pushed onto the stack. When a closing bracket is encountered, the top opening bracket is popped off the stack. If a closing bracket is encountered when the stack is empty, it means that there's no corresponding opening bracket, so the function returns False. If the function finishes iterating over the string without returning False, it returns True if the stack is empty (meaning every opening bracket was closed), and False otherwise (meaning there are unclosed opening brackets).
```python
def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
    brackets (str): A string of "<" and ">".

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.

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
            if not stack:  # If the stack is empty, there's no corresponding opening bracket
                return False
            stack.pop()
    return not stack  # If the stack is empty, all brackets were correctly matched


if __name__ == "__main__":
    print(correct_bracketing("<"))  # False
    print(correct_bracketing("<>"))  # True
    print(correct_bracketing("<<><>>"))  # True
    print(correct_bracketing("><<>"))  # False
```

This script uses a stack to keep track of opening brackets. It iterates over the string of brackets, pushing opening brackets onto the stack and popping them off when it encounters a closing bracket. If it ever tries to pop from an empty stack (meaning there's no corresponding opening bracket for a closing bracket), it immediately returns `False`. After iterating over the entire string, it returns whether the stack is empty (meaning all brackets were correctly matched) or not.
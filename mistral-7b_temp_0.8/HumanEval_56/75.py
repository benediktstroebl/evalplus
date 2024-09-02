

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
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
    # TODO: Fix the following to return the correct result.
    # You may need to write additional helper functions.
    if len(brackets) % 2 != 0:
        return False
    stack = []
    for char in brackets:
        if char == "<":
            stack.append(">")
        elif char == ">":
            stack.pop()
        else:
            return False
    return True


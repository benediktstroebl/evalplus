

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
    brackets_stack = []
    for bracket in brackets:
        if bracket == "<":
            brackets_stack.append("<")
        if bracket == ">":
            if not brackets_stack:
                return False
            brackets_stack.pop()
    return not brackets_stack

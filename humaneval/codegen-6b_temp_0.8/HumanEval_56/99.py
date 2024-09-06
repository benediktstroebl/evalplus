

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
    left_stack = []
    for bracket in brackets:
        if bracket == "<":
            left_stack.append(">")
        elif bracket == ">":
            if not left_stack:
                return False
            if left_stack.pop() != bracket:
                return False
    return not left_stack


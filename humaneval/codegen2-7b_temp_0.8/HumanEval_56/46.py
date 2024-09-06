

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
    bracket_stack = []
    for c in brackets:
        if c == "<":
            if bracket_stack and bracket_stack[-1] == ">":
                bracket_stack.pop()
            else:
                return False
        elif c == ">":
            bracket_stack.append(c)
    return not bracket



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
    if not brackets:
        return True

    bracket_stack = []
    for i, bracket in enumerate(brackets):
        if bracket == "<":
            if not bracket_stack or bracket_stack[-1]!= ">":
                return False
            bracket_stack.pop()
        else:
            bracket_stack.append(bracket)
    return len(bracket_stack) ==

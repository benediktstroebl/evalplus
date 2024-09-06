

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
    for bracket in brackets:
        if bracket == ">" or bracket == "<":
            if len(bracket_stack) == 0:
                return False
            elif bracket == ">" and bracket_stack[-1] == "<":
                return False
            elif bracket == "<" and bracket_stack[-1] == ">":
                return False
            else:
                bracket_stack.append(bracket)
    return len(bracket_stack) == 0

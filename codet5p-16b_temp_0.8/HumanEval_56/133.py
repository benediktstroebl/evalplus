

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

    if len(brackets) == 1:
        return True
    elif len(brackets) % 2 == 1:
        return False
    else:
        bracket_stack = []
        for bracket in brackets:
            if bracket == ">":
                if bracket_stack:
                    bracket_stack.pop()
                else:
                    return False
            else:
                bracket_stack.append(bracket)
        return not bracket_stack

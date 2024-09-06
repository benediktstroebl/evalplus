

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
    if len(brackets) % 2 != 0:
        return False
    opening_brackets = []
    for bracket in brackets:
        if bracket == "<":
            opening_brackets.append(bracket)
        elif bracket == ">":
            if opening_brackets:
                opening_brackets.pop()
            else:
                return False
    if opening_brackets:
        return False
    else:
        return True


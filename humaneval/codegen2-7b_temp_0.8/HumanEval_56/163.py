

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
    opening = []
    closing = []
    for i in range(0,len(brackets)):
        if brackets[i] == ">":
            closing.append(brackets[i])
        else:
            opening.append(brackets[i])
    if len(opening)!= len(closing):
        return False
    else:
        return True
    



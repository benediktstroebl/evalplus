

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
    for bracket in brackets:
        if bracket not in ["<", ">"]:
            return False
        if bracket == "<":
            while bracket.startswith("<"):
                bracket = bracket.replace("<", "")
                if bracket == ">":
                    return True
        elif bracket == ">":
            while bracket.endswith(">"]):
                bracket = bracket[:-2]
                if bracket == "<":
                    return True
        else:
            return False
    return True



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
            if not bracket.lower() in [">"]:
                return False
        if bracket == ">":
            if not bracket.lower() in ["<", "="]:
                return False
        if bracket == "=":
            if not brackets.count(bracket.lower()) % 2 == 0:
                return False
    return True
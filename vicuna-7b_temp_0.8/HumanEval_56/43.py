

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
        if bracket not in ("<", ">":
            return False
        if bracket == "<":
            next_bracket = brackets[brackets.find(bracket)+1]
            if next_bracket == ">":
                return True
            if next_bracket == "<":
                return False
        if bracket == ">":
            next_bracket = brackets[brackets.find(bracket)-1]
            if next_bracket == "<":
                return True
            if next_bracket == ">":
                return False
    return True

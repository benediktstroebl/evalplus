

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    opening_bracket = ""
    for bracket in brackets:
        if bracket == "(":
            opening_bracket += "("
        else:
            if opening_bracket!= "":
                opening_bracket = opening_bracket[:-1]
            else:
                return False
    return opening_bracket == ""




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
    opening_brackets = []
    for s in brackets:
        if s == "(":
            opening_brackets.append(s)
        elif s == ")":
            if opening_brackets:
                opening_brackets.pop()
            else:
                return False
    return not opening_brackets

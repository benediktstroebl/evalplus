

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

    pars = []
    for char in brackets:
        if char == "(":
            pars.append(char)
        elif char == ")":
            if len(pars) > 0:
                pars.pop()
            else:
                return False
    return len(pars) == 0

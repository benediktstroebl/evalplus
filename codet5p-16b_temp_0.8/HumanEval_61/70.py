

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

    openings = []
    for char in brackets:
        if char == "(":
            openings.append(char)
        elif char == ")":
            if len(openings) == 0:
                return False
            openings.pop()
    if len(openings)!= 0:
        return False
    return True

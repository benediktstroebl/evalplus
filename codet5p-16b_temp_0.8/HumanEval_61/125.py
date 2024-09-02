

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

    assert len(brackets) > 0

    correct = True
    openings = []
    for i, c in enumerate(brackets):
        if c == "(":
            openings.append(i)
        elif c == ")":
            if len(openings) > 0:
                openings.pop()
            else:
                correct = False
                break
    if openings:
        correct = False
    return correct


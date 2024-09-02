

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
    next_open = []
    if len(brackets) == 0:
        return False
    if len(brackets) % 2 != 0:
        return False
    for brackets in brackets:
        if brackets == "(":
            next_open.append(brackets)
        elif brackets == ")":
            if len(next_open) == 0:
                return False
            if next_open[-1] == "(":
                del next_open[-1]
    if len(next_open) == 0:
        return True

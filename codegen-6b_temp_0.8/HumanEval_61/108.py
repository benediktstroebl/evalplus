

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
    lst = []
    i = 0
    while i < len(brackets):
        if brackets[i] == "(":
            lst.append("(")
        elif brackets[i] == ")":
            if len(lst) == 0:
                return False
            else:
                lst.pop()
        i += 1
    return len(lst) == 0


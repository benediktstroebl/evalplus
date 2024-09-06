

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

    brackets_open = []
    for bracket in brackets:
        if bracket == "(":
            brackets_open.append(bracket)
        else:
            if len(brackets_open) == 0:
                return False
            brackets_open.pop()

    return len(brackets_open) == 0

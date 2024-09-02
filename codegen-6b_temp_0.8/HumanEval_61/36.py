

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
    assert isinstance(brackets, str)
    brackets = brackets.replace("()", "")
    if len(brackets) == 0:
        return True

    start_bracket = None
    for bracket in brackets:
        if bracket == "(":
            start_bracket = bracket
            continue
        elif start_bracket is None:
            return False
        else:
            start_bracket = None

    if start_bracket is not None:
        return False

    return True


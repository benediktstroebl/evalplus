

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
    # TODO: I think we can do this without using a stack
    results = []
    for bracket in brackets:
        if bracket == '(':
            results.append(True)
        elif bracket == ')':
            if len(results) == 0:
                return False
            results.pop()
    return len(results) == 0
        
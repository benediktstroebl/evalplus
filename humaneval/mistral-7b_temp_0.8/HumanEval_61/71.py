

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
    closings = []

    for char in brackets:
        if char == '(':
            openings.append('(')
        elif char == ')':
            closings.append(')')
        else:
            return False

    if openings == closings:
        return True
    else:
        return False


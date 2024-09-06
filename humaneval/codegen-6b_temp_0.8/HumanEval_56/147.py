

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    if not brackets:
        return True
    if not brackets[0] in ['<', '>']:
        return False
    matches = []
    for index, bracket in enumerate(brackets):
        if bracket == '<':
            matches.append('>')
        else:
            if matches:
                matches.pop()
            else:
                return False
    return True


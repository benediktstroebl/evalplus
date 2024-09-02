

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

    openings = []

    for index in range(len(brackets)):
        if brackets[index] == '<':
            openings.append(index)
        if brackets[index] == '>':
            if not openings:
                return False
            openings.pop()

    if not openings:
        return True
    else:
        return False


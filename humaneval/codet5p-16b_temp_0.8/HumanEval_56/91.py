

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

    brackets = list(brackets)
    openings = []
    for i in range(len(brackets)):
        if brackets[i] == '<':
            openings.append(i)
        elif brackets[i] == '>':
            if len(openings) == 0:
                return False
            openings.pop()
    if len(openings) == 0:
        return True
    return False


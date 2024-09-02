

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
    if brackets[0] == ">" or not brackets:
        return False
    if brackets[0] == "<":
        return correct_bracketing(brackets[1:])
    left_bracket = 0
    for index in range(1, len(brackets)):
        if brackets[index] == "<":
            left_bracket += 1
        elif brackets[index] == ">":
            left_bracket -= 1
        if left_bracket < 0:
            return False
    return left_bracket == 0





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
    if len(brackets) == 0:
        return True
    # TODO
    opening_bracket = "<"
    closing_bracket = ">"

    count = 0
    for i in range(0, len(brackets)):
        if opening_bracket in brackets[i]:
            count = count + 1
        if closing_bracket in brackets[i]:
            count = count - 1
        if count < 0:
            return False
    return count == 0


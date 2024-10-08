

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
    valid = True
    for i in range(len(brackets)):
        if i < len(brackets) - 1 and brackets[i]!= brackets[i + 1]:
            valid = False
            break
    return valid


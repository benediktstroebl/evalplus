

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
    for i in range(len(brackets)):
        if brackets[i] == "<" and not bracket_has_closing_brace(brackets, i+1):
            return False
        if brackets[i] == ">" and not bracket_has_opening_brace(brackets, i-1):
            return False
    return True



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
    opening = '<'
    closing = '>'
    start = 0
    while True:
        if (start == len(brackets)):
            return True
        if (brackets[start] == opening):
            if (opening == closing):
                return True 
            else:
                return False
        else:
            start += 1

    pass

    return True

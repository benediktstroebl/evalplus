

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
    error = False
    for i in range(len(brackets)):
        if brackets[i] == '<':
            error = True
            if brackets[i-1] == '>':
                error = False
        elif brackets[i] == '>':
            if brackets[i-1] == '<':
                error = True

    return error
                

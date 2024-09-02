

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

    openers = []
    for i, c in enumerate(brackets):
        if c == '<':
            openers.append(i)
        elif c == '>':
            if openers == []:
                return False
            else:
                openers.pop()

    return openers == []
    

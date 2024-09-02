

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
    while brackets:
        if "<" not in brackets:
            return False
        bracket = ">"
        i = brackets.index(bracket)
        if "<" == brackets[i+1]:
            brackets = brackets[:i] + brackets[i+2:]
        elif "<" == brackets[i-1]:
            brackets = brackets[:i-1] + brackets[i+1:]
        else:
            return False
    return True




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
    open_brackets = set(brackets.split("<>"))
    for open_bracket in open_brackets:
        for i in range(1, len(open_brackets)):
            if open_brackets[i - 1] == open_brackets[i]:
                return False
    return True

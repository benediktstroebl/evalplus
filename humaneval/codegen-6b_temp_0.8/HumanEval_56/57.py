

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
    count = {}
    for i in range(len(brackets)):
        if brackets[i] == "<":
            count[brackets[i]] = "<"
        elif brackets[i] == ">":
            if brackets[i-1] == "<":
                count.pop(brackets[i])
            else:
                count[brackets[i]] = ">"
    if count == {}:
        return True
    else:
        return False

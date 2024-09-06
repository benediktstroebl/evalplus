

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
    count = 0
    for i in range(len(brackets)):
        if brackets[i] == "<":
            if not bracket_exists(brackets, i+1):
                count += 1
            else:
                i += 1
        elif brackets[i] == ">":
            if not bracket_exists(brackets, i-1):
                count += 1
            else:
                i -= 1
    return count == 0

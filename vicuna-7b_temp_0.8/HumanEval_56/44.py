

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
    # check if the string is empty
    if not brackets:
        return True

    # check if the string only contains one bracket
    if len(brackets) == 1:
        if brackets[0] == ">":
            return True
        else:
            return False

    # check if the string contains two brackets that are next to each other
    for i in range(1, len(brackets)):
        if brackets[i-1] != brackets[i]:
            return False

    # check if the string contains the same number of open and closed brackets
    count = 0
    for bracket in brackets:
        if bracket == ">":
            count += 1
        elif bracket == "<":
            count -= 1

    return count == 0
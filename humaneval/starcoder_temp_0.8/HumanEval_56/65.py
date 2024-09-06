

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
    if len(brackets) % 2!= 0:
        return False
    else:
        left = 0
        right = 0
        for i in range(len(brackets)):
            if brackets[i] == "<":
                left += 1
            elif brackets[i] == ">":
                right += 1
            if left!= right:
                return False
        return True


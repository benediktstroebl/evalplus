

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

    # your code here
    my_list = list(brackets)
    for i in range(len(brackets)):
        if brackets[i] == "<":
            if brackets[i + 1] == ">":
                pass
            else:
                return False

    return True



















































































































































































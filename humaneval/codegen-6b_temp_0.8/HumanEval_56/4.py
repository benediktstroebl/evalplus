

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
    flag = True
    left = []
    right = []
    for i in brackets:
        if i == "<":
            left.append(i)
        elif i == ">":
            if len(left) == 0:
                return False
            c = left.pop()
            if c != "<":
                return False
            right.append(i)
        else:
            left.append(i)
    if len(left) > 0:
        flag = False
    if len(right) > 0:
        flag = False

    return flag



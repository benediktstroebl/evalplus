

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
    stack = []
    for item in brackets:
        if item == '<':
            stack.append(item)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    if stack == []:
        return True
    else:
        return False



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
    # This is a fun one.  At the end of it, your stack should contain
    # nothing or only one value.  If nothing, you have balanced the
    # brackets.  If only one value, that value should be a ">".
    stack = []
    for char in brackets:
        if char == "<":
            stack.append(char)
        else:
            if stack == []:
                return False
            stack.pop()
    if stack == []:
        return True
    else:
        return False

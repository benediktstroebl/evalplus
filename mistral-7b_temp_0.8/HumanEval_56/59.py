

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

    stk = []
    brackets = brackets.replace("<<>", "<>")

    for ch in brackets:
        if ch == "<":
            stk.append(ch)
        elif ch == ">":
            if stk:
                stk.pop()
            else:
                return False
    if stk:
        return False
    else:
        return True


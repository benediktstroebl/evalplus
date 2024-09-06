

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

    assert all(bracket in "<>" for bracket in brackets)
    i = 0
    j = 0
    stack = []
    while i < len(brackets):
        if brackets[i] == "<":
            stack.append(i)
        elif brackets[i] == ">":
            if not stack:
                return False
            else:
                j = stack.pop()
                if i == j:
                    return False
        i += 1
    return True

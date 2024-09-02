

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

    bracketing = []
    for i, b in enumerate(brackets):
        if b == "<":
            bracketing.append(i)
        elif b == ">":
            if bracketing and bracketing[-1] == i - 1:
                bracketing.pop()
            else:
                bracketing.append(i)
    return bracketing == []

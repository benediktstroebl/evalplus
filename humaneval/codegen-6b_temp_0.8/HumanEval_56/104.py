

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
    parens = []
    for b in brackets:
        if b == "<":
            parens.append(b)
        elif len(parens) == 0:
            return False
        elif b == ">":
            prev_paren = parens.pop()
            if prev_paren != "<":
                return False
    return True

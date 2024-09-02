

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
    brackets = list(brackets)
    for i, c in enumerate(brackets):
        if c == '<':
            if brackets[i-1] == '<':
                brackets[i-1] = '>'
            else:
                return False
    return all(c == '>' for c in brackets)

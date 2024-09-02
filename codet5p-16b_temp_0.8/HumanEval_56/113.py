

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

    open_brackets = []
    for c in brackets:
        if c == '<':
            open_brackets.append(c)
        elif c == '>':
            if not open_brackets:
                return False
            open_brackets.pop()
    return not open_brackets

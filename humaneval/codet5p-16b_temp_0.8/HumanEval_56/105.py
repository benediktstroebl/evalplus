

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
    for b in brackets:
        if b == '<':
            open_brackets.append(b)
        elif b == '>':
            if open_brackets == []:
                return False
            open_brackets.pop()
    return open_brackets == []

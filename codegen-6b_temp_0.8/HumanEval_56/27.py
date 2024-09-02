

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
    assert type(brackets) == str
    assert len(brackets) % 2 == 0
    lst = []
    for c in brackets:
        if c == '<':
            lst.append('>')
        else:
            assert c == '>'
            if len(lst) == 0:
                return False
            lst.pop()
    if len(lst) == 0:
        return True
    else:
        return False

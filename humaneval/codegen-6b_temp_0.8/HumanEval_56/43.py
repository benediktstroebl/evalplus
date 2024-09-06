

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
    assert not brackets or all([x == '<' or x == '>' for x in brackets])
    if not brackets: 
        return True
    anchor = 0
    for i in range(1, len(brackets)):
        if brackets[i] == '<':
            anchor += 1
        else:
            anchor -= 1
        if anchor < 0:
            return False
    return True

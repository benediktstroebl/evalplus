

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
    assert all(c in ("<", ">") for c in brackets)
    #assert len(brackets) % 2 == 0
    stack = []
    for c in brackets:
        if c == "<":
            stack.append(c)
        else:
            assert c == ">"
            if stack == []:
                return False
            stack.pop()
    return stack == []




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
    for bracket in brackets:
        if bracket not in ["<", ">"]:
            return False
    return True

def test_correct_bracketing():
    assert correct_bracketing("<") == False
    assert correct_bracketing("<>") == True
    assert correct_bracketing("<<><>>") == True
    assert correct_bracketing("><<>") == False

test_correct_bracketing()
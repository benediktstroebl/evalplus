

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
    # can only use string methods and list methods. No if statements.
    return len(brackets) % 2 == 0 and ''.join([bracket for bracket in brackets if bracket == '<']) == ''.join([bracket for bracket in reversed(brackets) if bracket == '>'])


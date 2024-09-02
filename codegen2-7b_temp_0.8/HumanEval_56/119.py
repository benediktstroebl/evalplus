

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
    assert brackets[0] == "<" and brackets[-1] == ">", "must be valid input"
    brackets = list(brackets)
    while brackets:
        if brackets[0] == "<" and brackets[1] == ">":
            brackets.pop(0)
            brackets.pop(0)
        elif brackets[0] == ">":
            brackets.pop(0)
        else:
            return False
    return

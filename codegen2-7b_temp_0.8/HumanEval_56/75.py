

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
    assert len(brackets) % 2 == 0
    closing_brackets = {">": "<", "<": ">"}
    for i in range(0, len(brackets) // 2):
        if brackets[i]!= closing_brackets[brackets[i + 1]]:
            return False
    

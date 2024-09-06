

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
    closes = {
        ">": "<",
        "<": ">",
        ">": ">>",
        ">>": "<<"
    }
    if len(brackets) % 2!= 0:
        return False
    for i in range(0, len(brackets) // 2):
        if not closes[brackets[i]] == brackets[len(brackets) - 1 - i]:
            return False
    return

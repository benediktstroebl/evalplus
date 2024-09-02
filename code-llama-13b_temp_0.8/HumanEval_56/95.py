

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
    balance = 0
    for b in brackets:
        if b == '<':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0




def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    if len(brackets) % 2 == 1:
        return False
    balance = 0
    for c in brackets:
        if c == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                return False
    return balance == 0


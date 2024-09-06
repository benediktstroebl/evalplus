

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
    # Your code here
    balance = 0
    for i in brackets:
        if i == "(":
            balance += 1
        if i == ")":
            balance -= 1
        if balance < 0:
            return False
    if balance > 0:
        return False
    return True



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

    balance = 0  # keep a balance of unmatched left vs right

    for i in range(len(brackets)):
        if brackets[i] == '(':
            balance += 1
        elif brackets[i] == ')' and balance > 0:
            balance -= 1
        else:
            return False
    return balance == 0


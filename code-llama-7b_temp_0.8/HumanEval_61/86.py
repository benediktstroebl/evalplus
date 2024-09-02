

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
    # this implementation is wrong
    # it gives the wrong answer for the string "(()()"
    # the error is in the code after the return statement

    balance = 0
    for i in range(len(brackets)):
        if brackets[i] == "(":
            balance += 1
        elif brackets[i] == ")":
            balance -= 1
        if balance < 0:
            return False
    return balance == 0


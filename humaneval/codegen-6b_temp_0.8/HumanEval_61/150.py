

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
    "*** YOUR CODE HERE ***"

    openers = 0
    for i in range(len(brackets)):
        if brackets[i] == "(":
            openers += 1
        else:
            openers -= 1
        if openers == -1:
            return False

    if openers == 0:
        return True
    else:
        return False
    

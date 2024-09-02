

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
    # first idea is to use a loop that counts the amount of "(" and ")"
    # loop as long as there are any brackets left
    # everytime it loops add one to the amount of "("
    # everytime it loops subtract one from the amount of ")"
    # if there are any remaining brackets then return False
    # if the amount of "(" and ")" are equal then return True
    # if the amount of ")" is greater than the amount of "(" then return False

    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


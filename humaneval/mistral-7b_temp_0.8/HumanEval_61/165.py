

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
    opening_bracket = "("
    closing_bracket = ")"
    counter = 0
    brackets = [brackets[i] for i in range(len(brackets))]

    for bracket in brackets:
        if bracket == opening_bracket:
            counter += 1
        elif bracket == closing_bracket:
            counter -= 1
        if counter < 0:
            return False

    if counter == 0:
        return True
    else:
        return False



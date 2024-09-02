

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

    opened_brackets = 0
    closed_brackets = 0

    for character in brackets:
        if character == '(':
            opened_brackets += 1
        elif character == ')':
            closed_brackets += 1

        if closed_brackets > opened_brackets:
            return False

    if opened_brackets == closed_brackets:
        return True
    else:
        return False


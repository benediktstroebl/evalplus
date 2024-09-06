

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
    if not brackets:
        return True

    opening_brackets = []
    for i, bracket in enumerate(brackets):
        if bracket == "(":
            opening_brackets.append(i)

        if bracket == ")":
            if not opening_brackets:
                return False

            opening_brackets.pop()

    return not opening_brackets




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
    for bracket in brackets:
        if bracket == "(":
            current = "("
        else:
            current = ")"

        # Go through the remaining brackets.
        for next_bracket in brackets[brackets.index(bracket) + 1:]:
            if current == "(" and next_bracket == ")":
                return True
            if current == ")" and next_bracket == "(":
                return False

    return True


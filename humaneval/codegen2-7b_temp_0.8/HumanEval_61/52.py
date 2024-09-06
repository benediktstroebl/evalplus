

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
    brackets = brackets.replace(" ", "")
    bracket_count = 0
    for bracket in brackets:
        if bracket == "(":
            bracket_count += 1
        elif bracket == ")":
            if bracket_count == 0:
                return False
            bracket_count -= 1
    if bracket_count == 0:
        return True
    return False

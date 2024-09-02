

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

    brackets = list(brackets)
    open_bracket_count = 0
    close_bracket_count = 0

    for bracket in brackets:
        if bracket == '(':
            open_bracket_count += 1
        else:
            close_bracket_count += 1

        if close_bracket_count > open_bracket_count:
            return False
    
    if close_bracket_count == open_bracket_count:
        return True
    else:
        return False

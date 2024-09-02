

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
    list_brackets = list(brackets)
    list_brackets.reverse()
    while list_brackets:
        if is_correct:
            return True
        elif is_not_correct:
            return False
        else:
            list_brackets.pop()
    return True

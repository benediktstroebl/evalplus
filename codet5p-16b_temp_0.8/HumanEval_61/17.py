

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

    opened_brackets = []
    for bracket in brackets:
        if bracket == '(':
            opened_brackets.append(bracket)
        else:
            if not opened_brackets:
                return False
            else:
                opened_brackets.pop()
    return not opened_brackets


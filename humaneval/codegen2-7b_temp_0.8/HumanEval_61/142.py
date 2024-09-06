

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
    if len(brackets) == 0:
        return True
    open_brackets = [c for c in brackets if c == '(']
    if len(open_brackets) == 0:
        return False
    open_bracket = open_brackets[-1]
    return open_bracket == ')' and correct_bracketing(brackets[:-1])

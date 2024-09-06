

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
    open_brackets = []
    for i, c in enumerate(brackets):
        if c == '(':
            open_brackets.append(i)
        elif c == ')' and len(open_brackets) > 0:
            open_bracket = open_brackets.pop()
            if i - open_bracket != 1:
                return False
    return True

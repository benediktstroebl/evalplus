

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
    # Your code here
    if brackets[0] == ")" or len(brackets) == 1:
        return False
    else:
        a = brackets.index(")")
        if a+1 == len(brackets):
            return True
        else:
            return correct_bracketing(brackets[a+1:])

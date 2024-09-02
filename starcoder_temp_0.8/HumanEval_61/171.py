

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
    open_brackets = [b for b in brackets if b == "(":]
    close_brackets = [b for b in brackets if b == ")"]
    return len(open_brackets) == len(close_brackets)

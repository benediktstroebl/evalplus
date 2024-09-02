

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
    open_brackets = set(brackets.split('('))
    closed_brackets = set(brackets.split(')'))
    
    if len(open_brackets) != len(closed_brackets):
        return False
    
    for open_bracket in open_brackets:
        if open_bracket not in closed_brackets:
            return False
    
    return True

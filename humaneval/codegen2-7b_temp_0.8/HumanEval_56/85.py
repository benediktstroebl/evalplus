

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    for open_bracket in brackets:
        if open_bracket not in '<>':
            raise ValueError("Found an unexpected opening bracket")
    for closing_bracket in brackets:
        if closing_bracket not in '<>':
            raise ValueError("Found an unexpected closing bracket")
    for pair in itertools.combinations(brackets, 2):
        if pair[0] == pair[1]:
            return False
    

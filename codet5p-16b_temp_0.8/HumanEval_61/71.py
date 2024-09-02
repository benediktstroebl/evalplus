

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

    
    pending_open_brackets = []
    
    for index, bracket in enumerate(brackets):
        if bracket == ")":
            if not pending_open_brackets:
                return False
            if pending_open_brackets[-1] == "(":
                pending_open_brackets.pop()
                continue
            else:
                return False
        elif bracket == "(" :
            pending_open_brackets.append(bracket)
    return True

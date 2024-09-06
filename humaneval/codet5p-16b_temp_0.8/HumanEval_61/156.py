

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

    
    openings = brackets.count("(")
    closings = brackets.count(")")
    
    if openings > closings:
        return False
    elif openings == closings:
        return True
    else:
        for i in range(len(brackets)):
            if brackets[i] == "(":
                if brackets[i+1]!= ")":
                    return False
        return True


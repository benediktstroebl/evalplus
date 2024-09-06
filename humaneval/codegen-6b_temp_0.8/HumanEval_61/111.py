

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
    
    left_brackets = 0
    for i in range(len(brackets)):
        if brackets[i] == "(":
            left_brackets += 1
        else:
            left_brackets -= 1
        
        if left_brackets < 0:
            return False
    
    return True
    

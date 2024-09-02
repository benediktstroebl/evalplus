

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

    
    brackets = list(brackets)
    open_brackets = []
    
    for index, bracket in enumerate(brackets):
        if bracket == "(":
            open_brackets.append(index)
        elif bracket == ")":
            if not open_brackets:
                return False
            
            open_brackets.pop()
        
    return len(open_brackets) == 0

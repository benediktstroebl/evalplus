

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
    
    left_brackets = [i for i, b in enumerate(brackets) if b == "<"]
    right_brackets = [i for i, b in enumerate(brackets) if b == ">"]
    
    current_level = 0
    
    if len(left_brackets) != len(right_brackets):
        return False
    
    for idx, bracket in enumerate(left_brackets):
        if bracket > current_level:
            current_level += 1
        elif bracket < current_level:
            current_level -= 1
        else:
            if idx == len(left_brackets) - 1:
                return True
    
    return True
    
    
    


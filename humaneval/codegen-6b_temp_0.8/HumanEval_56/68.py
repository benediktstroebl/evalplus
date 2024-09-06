

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
    
    while len(brackets) != 0:
        open_bracket = brackets[0]
        if open_bracket == ">" and brackets[1] != "<":
            return False
        else:
            brackets = brackets[1:]

    return True
        

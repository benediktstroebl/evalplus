

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
    
    opened_brackets = []
    for bracket in brackets:
        if opened_brackets and bracket == opened_brackets[-1]:
            opened_brackets.pop()
        else:
            opened_brackets.append(bracket)
    
    return len(opened_brackets) == 0

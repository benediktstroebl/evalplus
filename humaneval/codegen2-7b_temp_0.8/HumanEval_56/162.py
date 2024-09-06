

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
    
    left = brackets.count("<")
    right = brackets.count(">")
    if left == right and brackets.count("<>") == left:
        return True
    elif left == right and brackets.count("<<>>") == left:
        return True
    elif left!= right and brackets.count("<<>>") == right:
        return False
    else:
        

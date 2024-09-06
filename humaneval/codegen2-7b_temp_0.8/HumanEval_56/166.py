

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
    if not brackets:
        return False
    stack = []
    for char in brackets:
        if char in "()[]<>":
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if char!= top:
                return False
    if stack:
        return False
    return True
    



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
        return True
    
    bracket_stack = []
    open_brackets = set("<")
    closing_brackets = set(">")

    for bracket in brackets:
        if bracket in open_brackets:
            bracket_stack.append(bracket)
        elif bracket in closing_brackets:
            if not bracket_stack or bracket_stack.pop() != bracket:
                return False

    return not bracket_stack



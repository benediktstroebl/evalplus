

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

    
    bracket_count = {}
    for bracket in brackets:
        bracket_count[bracket] = bracket_count.get(bracket, 0) + 1
        
    bracket_stack = []
    for bracket in brackets:
        if bracket in "<":
            bracket_stack.append(bracket)
        else:
            if len(bracket_stack) == 0:
                return False
            if bracket_stack[-1] == "<":
                bracket_stack.pop()
            else:
                return False
    if len(bracket_stack) == 0:
        return True
    else:
        return False

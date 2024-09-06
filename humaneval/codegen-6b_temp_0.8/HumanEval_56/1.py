

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
    
    result = True;
    bracket_stack = []
    for char in brackets:
        if char == '<':
            bracket_stack.append('<')
        elif char == '>':
            if len(bracket_stack) > 0:
                bracket_stack.pop()
            else:
                # This is an error - dont return false
                result = False
    if len(bracket_stack) != 0:
        # This is an error - dont return false
        result = False
    return result



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

    # Your code here
    bracket_stack = []
    for b in brackets:
        if b == '<':
            bracket_stack.append('<')
        elif b == '>' and bracket_stack:
            bracket_stack.pop()
        else:
            return False
    return len(bracket_stack) == 0

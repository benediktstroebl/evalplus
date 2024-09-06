

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
    "*** YOUR CODE HERE ***"
    left_stack = []
    for b in brackets:
        if b == "<":
            left_stack.append(b)
        elif b == ">":
            if len(left_stack) == 0:
                return False
            left_stack.pop()
    return len(left_stack) == 0

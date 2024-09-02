

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
    opening, closing = "()", "()"
    opening_stack, closing_stack = [], []

    for bracket in brackets:
        if bracket == opening:
            opening_stack.append(bracket)
        elif bracket == closing:
            # if opening:
            #     opening_stack.pop()
            if not opening_stack:
                return False
            if opening_stack.pop() != closing:
                return False
    return True

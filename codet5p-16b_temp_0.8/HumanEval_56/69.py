

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

    bracket_pairs = {
        '<': '>',
        '>': '<'
    }
    bracket_stack = []
    for bracket in brackets:
        if bracket in bracket_pairs:
            bracket_stack.append(bracket)
        else:
            if not bracket_stack:
                return False
            top_bracket = bracket_stack.pop()
            if bracket_pairs[top_bracket]!= bracket:
                return False
    return not bracket_stack



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
    # Count the number of opening and closing brackets.
    # If they do not match, then we know that there is a mismatched bracket.
    open_brackets = 0
    close_brackets = 0
    for c in brackets:
        if c == '<':
            open_brackets += 1
        elif c == '>':
            close_brackets += 1
    return open_brackets == close_brackets

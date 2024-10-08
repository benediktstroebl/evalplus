

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

    
    opening_brackets = 0

    for char in brackets:
        if char == '<':
            opening_brackets += 1
        elif char == '>':
            opening_brackets -= 1

    if opening_brackets == 0:
        return True
    else:
        return False

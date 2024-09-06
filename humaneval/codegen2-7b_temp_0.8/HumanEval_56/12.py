

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
    brackets = list(brackets)
    index = 0
    while index < len(brackets):
        if index > 0 and brackets[index-1]!= '<' and brackets[index]!= '>':
            return False
        index += 1
    return

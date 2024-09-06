

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

    # open_brackets: List[str]
    open_brackets = []
    for b in brackets:
        if b == '<':
            open_brackets.append(b)
        elif b == '>' and open_brackets:
            open_brackets.pop()
        elif b == '>':
            return False
    return not open_brackets


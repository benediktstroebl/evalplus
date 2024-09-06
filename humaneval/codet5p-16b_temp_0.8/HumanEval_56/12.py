

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

    opening = []
    closing = []
    for i, c in enumerate(brackets):
        if c == '<':
            opening.append(i)
        if c == '>':
            closing.append(i)
    opening.append(len(brackets))
    closing.append(len(brackets))

    bracket_open = True
    for i in range(len(opening)):
        if bracket_open:
            if opening[i] in closing:
                bracket_open = False
        else:
            if closing[i] in opening:
                bracket_open = True

    return not bracket_open

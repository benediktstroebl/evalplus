

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
    left = re.finditer("<", brackets)
    right = re.finditer(">", brackets)

    match_left = []
    match_right = []
    for match in left:
        match_left.append(match.group())
    for match in right:
        match_right.append(match.group())

    return set(match_left) == set(match_right

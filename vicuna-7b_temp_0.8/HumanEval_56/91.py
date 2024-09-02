

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
    # first, convert the string to a set of bracket pairs
    bracket_pairs = set(brackets.split(">") + bracket_re.split("<>") + [""] * 2)

    # check if every bracket pair has a corresponding pair
    for i in range(len(bracket_pairs)):
        if bracket_pairs[i] != bracket_pairs[i + 1]:
            return False
    return True

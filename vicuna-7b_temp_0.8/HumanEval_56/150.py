

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
    # Convert the string to a set of tuples where the first element of the tuple is the bracket and the second element is None
    brackets_set = set(brackets.split(">") + brackets.split("<"))
    for bracket in brackets_set:
        if bracket != "<" and bracket != ">":
            return False
    return True

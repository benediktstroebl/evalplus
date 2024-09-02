

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
    # Base case:
    if len(brackets) == 0:
        return True
    if brackets[0] == '<':
        # Recursive case:
        # If there is at least one closing bracket after the first element, and the remaining string is
        # correct bracketing, we are good to go.
        if '>' in brackets[1:] and correct_bracketing(brackets[brackets.index('>') + 1:]):
            return True
        # If there is no closing bracket after the first element, return false.
        else:
            return False
    else:
        # The first element is not a '<', so we just ignore it and continue.
        return correct_bracketing(brackets[1:])

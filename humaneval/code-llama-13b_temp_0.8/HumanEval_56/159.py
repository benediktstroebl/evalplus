

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

    # Hint: Use the 'count' method on strings


    # convert the string of brackets to a list of individual characters
    # then remove the first and last characters (to get rid of the end brackets)
    # then, count how many ">" characters are in the string

    return True

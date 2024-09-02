

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

    # Want to check for two conditions:
    #   1) We've opened a bracket and closed a bracket,
    #   2) The same bracket has not been closed before it was opened.
    # We'll check condition 1 by keeping track of how many opened brackets
    # we've encountered as we loop through the string.
    # Condition 2 will be checked automatically, because we're using the
    # built-in str.count() function.

    return brackets.count("<") == brackets.count(">")


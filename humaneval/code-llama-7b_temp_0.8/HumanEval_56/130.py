

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
    # YOUR CODE HERE
    def is_closed(brackets):
        return brackets.count(">") == len(brackets)

    def is_opened(brackets):
        return brackets.count("<") == len(brackets)

    if is_closed(brackets):
        return True

    if is_opened(brackets):
        return False

    new_bracket = brackets[0]
    return correct_bracketing(brackets[1:])


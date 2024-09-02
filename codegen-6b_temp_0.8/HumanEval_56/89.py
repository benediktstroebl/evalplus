

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
    while "<" in brackets:
        if "<" not in brackets:
            return False
        index = brackets.index("<")
        bracket = brackets[index]
        closing_bracket = bracket + brackets[index + 1]
        brackets = brackets.replace(closing_bracket, '')
        brackets = brackets.replace(bracket, '')
    return True

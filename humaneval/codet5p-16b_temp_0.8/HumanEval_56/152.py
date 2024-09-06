

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

    if len(brackets) == 0:
        return True
    if brackets[0] == "<":
        return False
    brackets = brackets.replace('<', '<*')
    return correct_bracketing(brackets.replace('*>', '>'))


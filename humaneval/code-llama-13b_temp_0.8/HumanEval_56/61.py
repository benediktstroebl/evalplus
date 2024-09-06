

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
    # You must use a stack

    if len(brackets) == 0:
        return True

    if brackets[0] == '>':
        return False

    for i in range(len(brackets) - 1):
        if brackets[i] == '<' and brackets[i + 1] == '>':
            brackets = brackets[:i] + brackets[i + 2:]
            return correct_bracketing(brackets)

    return False

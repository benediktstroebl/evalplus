

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
    # i points to next empty location
    i = 0
    # j points to next open bracket
    j = 0
    while j < len(brackets):
        if brackets[j] == '<':
            brackets = brackets[:j] + 'X' + brackets[j + 1:]
            i += 1
        if brackets[i] == '>':
            brackets = brackets[:i] + 'X' + brackets[i + 1:]
            i -= 1
        j += 1
    return brackets.replace('X', '') == ''


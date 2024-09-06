

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
    # Your code here
    openBracket = 0
    for i in brackets:
        if i == '<':
            openBracket += 1
        elif i == '>':
            openBracket -= 1
        if openBracket < 0:
            return False

    return openBracket == 0


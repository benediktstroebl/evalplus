

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

    open_brackets = []
    for index, character in enumerate(brackets):
        if character == '<':
            open_brackets.append(index)
        elif character == '>':
            if len(open_brackets) == 0:
                return False
            else:
                open_brackets.pop()
    return len(open_brackets) == 0


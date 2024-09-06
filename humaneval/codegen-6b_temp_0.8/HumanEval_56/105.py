

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
    
    openning_brackets = []
    for pos, letter in enumerate(brackets):
        if letter == "<":
            openning_brackets.append(pos)
        elif letter == ">":
            if len(openning_brackets) == 0:
                return False
            else:
                openning_brackets.pop()
    if len(openning_brackets) != 0:
        return False
    else:
        return True
    

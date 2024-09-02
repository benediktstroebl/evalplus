

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
    count = 0
    while True:
        if count < len(brackets):
            if brackets[count] == "<":
                count += 1
                continue
        elif count >= len(brackets):
            break
        if brackets[count] == ">":
            count += 1
        else:
            break
    return True if count == len(brackets) else False


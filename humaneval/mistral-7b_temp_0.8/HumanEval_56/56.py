

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
    open_brackets = ["<"]
    closed_brackets = ["<"]
    counter = 0
    for bracket in brackets:
        if bracket in open_brackets:
            open_brackets.append(bracket)
            counter += 1
        elif bracket in closed_brackets:
            closed_brackets.append(bracket)
            counter -= 1
    return counter == 0




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
    brackets_open = []
    brackets_closed = []
    for bracket in brackets:
        if bracket == "<":
            brackets_open.append(bracket)
        elif bracket == ">":
            if brackets_closed:
                brackets_closed.pop()
            else:
                brackets_open.append(bracket)
        else:
            raise Exception("Invalid bracket!")

    return brackets_open == brackets_closed

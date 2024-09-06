

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
    output = []

    if not brackets:
        return True

    for bracket in brackets:
        if output and bracket == ">" and output[-1] == "<":
            output.pop()
        else:
            output.append(bracket)

    return output == []


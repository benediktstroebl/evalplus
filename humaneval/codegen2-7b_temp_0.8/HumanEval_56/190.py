

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
    opens, closes = ["<", ">", "<<", ">>"], ["<", ">", "<<", ">>"]
    stack = []
    for bracket in brackets:
        if bracket in opens:
            stack.append(bracket)
        elif stack and bracket == closes[opens.index(stack[-1])]:
            stack.pop()
        else:
            return False
    return

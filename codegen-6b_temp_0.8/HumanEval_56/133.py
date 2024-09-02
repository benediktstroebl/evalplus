

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
    s = Stack()
    for bracket in brackets:
        if bracket == "<":
            s.push(bracket)
        elif bracket == ">":
            if s.isEmpty():
                return False
            else:
                s.pop()

    return s.isEmpty()

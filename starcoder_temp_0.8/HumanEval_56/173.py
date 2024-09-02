

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

    # your code here
    last_brackets = []
    for bracket in brackets:
        if bracket == "<":
            last_brackets.append(bracket)
        elif bracket == ">":
            if last_brackets:
                last_brackets.pop()
            else:
                return False
    return True

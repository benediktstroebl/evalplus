

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

    opening_brackets = []
    closing_brackets = []
    for b in brackets:
        if b == "<":
            opening_brackets.append(b)
        else:
            if not opening_brackets:
                return False
            else:
                opening_brackets.pop()
                closing_brackets.append(b)
    return len(opening_brackets) == 0

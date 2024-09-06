

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
    for bracket in brackets:
        if bracket not in ["<", ">"]:
            return False

        if bracket == "<":
            while bracket in brackets:
                if bracket == "<":
                    if brackets.count(bracket) > 1:
                        return False
                else:
                    brackets.remove(bracket)

        else:
            while bracket in brackets:
                if bracket == ">":
                    if brackets.count(bracket) > 1:
                        return False
                else:
                    brackets.remove(bracket)

    return True
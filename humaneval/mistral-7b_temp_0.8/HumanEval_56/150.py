

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
    opening_bracket = ">"
    closing_bracket = "<"
    brackets = list(brackets)
    if opening_bracket in brackets:
        brackets.remove(opening_bracket)
        if not opening_bracket in brackets:
            if closing_bracket in brackets:
                brackets.remove(closing_bracket)
                if not closing_bracket in brackets:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


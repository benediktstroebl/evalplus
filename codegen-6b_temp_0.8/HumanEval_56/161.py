

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
    "*** YOUR CODE HERE ***"
    if len(brackets)==0:
        return True
    if brackets[0]=="<":
        brackets=brackets[1:]
        return correct_bracketing(brackets)
    else:
        bracket=brackets[-1]
        brackets=brackets[:-1]
        if bracket==">" and brackets[-1]=="<":
            brackets=brackets[:-1]
            return  correct_bracketing(brackets)
        else:
            return False

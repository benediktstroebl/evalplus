

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

    # opening = 0
    # for b in brackets:
    #     if b == '<':
    #         opening += 1
    #     else:
    #         if opening:
    #             opening -= 1
    #         else:
    #             return False
    # if opening == 0:
    #     return True
    # return False
    return not (len(brackets.replace('<', '')) or len(brackets.replace('>', '')))


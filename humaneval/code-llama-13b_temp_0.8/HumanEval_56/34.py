

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
    #         opening -= 1
    #     if opening < 0:
    #         return False
    # return opening == 0

    # Opening and closing lists
    opens, closes = [], []

    for b in brackets:
        if b == '<':
            opens.append(b)
        elif b == '>':
            closes.append(b)

    return len(opens) == len(closes)


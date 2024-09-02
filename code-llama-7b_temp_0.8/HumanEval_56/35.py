

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
    # sequence is an integer list, where each odd-indexed element is a ">"
    # and each even-indexed element is a "<"
    sequence = []
    for ch in brackets:
        if ch == ">":
            sequence.append(1)
        else:
            sequence.append(-1)

    # reduce adds up the list. So long as the list is not empty,
    # the number is always even, so we have a valid bracketing.
    return len(sequence) % 2 == 0



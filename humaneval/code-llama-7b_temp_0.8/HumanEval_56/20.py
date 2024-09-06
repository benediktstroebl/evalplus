

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
    # '><' is a string with no opening brackets and one closing bracket.
    # '><<> is a string with no closing brackets and one opening bracket.
    # '<>' is a string with one opening bracket and one closing bracket.
    # '<><> is a string with two opening brackets and two closing brackets.

    # YOUR CODE HERE
    count = 0
    for i in brackets:
        if i == '<':
            count += 1
        elif i == '>':
            count -= 1
        if count < 0:
            return False
    return count == 0



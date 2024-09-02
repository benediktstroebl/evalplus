

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

    if len(brackets) % 2!= 0:
        return False

    count_bracket = [0, 0]

    for char in brackets:
        count_bracket[1] += 1 if char == '<' else -1
        count_bracket[0] += 1 if char == '>' else -1

        if count_bracket[0] < 0:
            return False
        if count_bracket[1] < 0:
            return False

    return count_bracket[0] == 0 and count_bracket[1] == 0

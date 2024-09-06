

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
    # Create a dictionary to count the number of opening and closing brackets
    count = {}
    for bracket in brackets:
        if bracket.startswith("<"):
            count["<"] += 1
        elif bracket.startswith(">") and count.get(bracket[2:], 0):
            count[bracket.replace(">", "", 1)] -= 1
    return count.get(brackets, 0) == 0

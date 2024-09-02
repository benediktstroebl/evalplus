

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
    count = 0
    #  iterate over string
    for char in brackets:
        #  if opening bracket
        if char == "<":
            count += 1
        #  if closing bracket
        elif char == ">":
            count -= 1
        #  if no match
        else:
            return False
    return count == 0


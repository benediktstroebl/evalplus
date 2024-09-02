

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
    # count is initially the number of open brackets we have seen
    count = 0
    # for each bracket in the string
    for b in brackets:
        if b == '>':
            count -= 1
        if b == '<':
            count += 1
        # if we have more closing brackets than opening ones
        if count < 0:
            return False
    # if we exited the loop normally, all brackets were closed
    return count == 0


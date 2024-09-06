

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    def count_open_close(s):
        count_open = 0
        count_close = 0
        for char in s:
            if char == "(":
                count_open += 1
            elif char == ")":
                count_close += 1
        return count_open, count_close

    count_open, count_close = count_open_close(brackets)
    if count_open == count_close:
        return True
    else:
        return False

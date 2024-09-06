

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
    "*** YOUR CODE HERE ***"

    def f(open_count: int):
        return True if open_count == 0 else False
    open_count = 0
    for b in brackets:
        if b == "(":
            open_count += 1
        else:
            open_count -= 1
        if open_count < 0:
            return False
    return f(open_count)




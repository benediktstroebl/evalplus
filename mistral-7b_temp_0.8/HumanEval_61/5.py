

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
    # your code here
    brackets_counter = 0
    for bracket in brackets:
        if bracket == '(':
            brackets_counter += 1
        else:
            brackets_counter -= 1

        if brackets_counter < 0:
            return False
    return brackets_counter == 0

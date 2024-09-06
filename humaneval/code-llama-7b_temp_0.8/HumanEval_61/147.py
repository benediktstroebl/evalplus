

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
    # old method, slow
    # return brackets.count("(") == brackets.count(")")

    # modified from https://github.com/ucsd-cse132/asg7.2021.spring/blob/main/correct_bracketing.py
    # find the index of first closing bracket, if it's before the first opening bracket, return false
    open_bracket_stack = []
    for i, b in enumerate(brackets):
        if b == '(':
            open_bracket_stack.append(i)
        elif b == ')':
            if len(open_bracket_stack) == 0:
                return False
            open_bracket_stack.pop()

    return True if len(open_bracket_stack) == 0 else False


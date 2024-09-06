

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
    brackets_list = list(brackets)
    stack = []
    for bracket in brackets_list:
        if bracket == "(":
            stack.append(bracket)
        elif not stack or stack.pop()!= bracket:
            return False
    return not stack


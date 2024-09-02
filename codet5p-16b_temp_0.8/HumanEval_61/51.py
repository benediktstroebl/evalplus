

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

    brackets_list = []
    for char in brackets:
        if char == "(":
            brackets_list.append(char)
        elif char == ")":
            brackets_list.pop()
    return not brackets_list


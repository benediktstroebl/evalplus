

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
    brackets_list_end = []
    brackets_list_begin = []

    for char in brackets_list:
        if char == "(":
            brackets_list_begin.append(char)
        else:
            brackets_list_end.append(char)

    brackets_list_end.reverse()

    for char in brackets_list_begin:
        if char != brackets_list_end[0]:
            return False
        else:
            brackets_list_begin.pop(0)
            brackets_list_end.pop(0)
    return True


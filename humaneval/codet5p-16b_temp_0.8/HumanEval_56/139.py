

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

    brackets_list = brackets.split('<')
    last = brackets_list[-1]
    if last == '':
        brackets_list = brackets_list[:-1]
    for bracket in brackets_list:
        if bracket == '':
            continue
        if bracket[0] == '>':
            return False
    return True

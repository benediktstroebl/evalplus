

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
    brackets_list = list(brackets)
    for i in range(len(brackets)):
        brackets_list[i] = brackets_list[i].replace('<', '')
        brackets_list[i] = brackets_list[i].replace('>', '')
    if brackets_list == ['<', '>']:
        return True
    else:
        return False



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

    my_list = []

    for i in brackets:
        if i == '<':
            my_list.append(i)
        elif i == '>':
            if len(my_list) == 0:
                return False
            else:
                my_list.pop()

    return len(my_list) == 0

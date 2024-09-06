

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
    correct_brackets = list(brackets)

    while True:
        opened = brackets_list.index('(')
        closed = brackets_list.index(')')

        if closed > opened:
            correct_brackets.pop(opened)
            correct_brackets.pop(opened - 1)
        else:
            return False

        brackets_list = list(correct_brackets)

        if len(brackets_list) == 1:
            return True


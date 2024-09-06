

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

    # This is a list, not a string.
    open_brackets = ['(', '[']

    # This is a string.
    close_brackets = ')', ']'

    # brackets_list = list(brackets)

    # print(brackets_list)

    for bracket in brackets:
        if bracket in open_brackets:
            brackets = brackets.replace(bracket, close_brackets[open_brackets.index(bracket)])

    # print(brackets)

    if brackets == "":
        return True
    else:
        return False





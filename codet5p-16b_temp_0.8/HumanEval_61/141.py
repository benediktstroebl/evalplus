

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
    brackets_list.append(brackets[0])
    for bracket in brackets[1:]:
        if bracket == ")" and brackets_list[-1] == "(":
            brackets_list.pop()
        else:
            brackets_list.append(bracket)
    return brackets_list == []

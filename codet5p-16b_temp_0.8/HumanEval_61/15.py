

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
    for index, bracket in enumerate(brackets_list):
        if bracket == ')':
            if brackets_list[index-1] == '(':
                brackets_list[index-1] = '2'
            elif brackets_list[index-1].isdigit():
                brackets_list[index-1] = int(brackets_list[index-1]) + 1
            else:
                return False
    print(brackets_list)
    return True if len(brackets_list) == sum(brackets_list) else False



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

    brackets_list = brackets.split()
    brackets_list = [bracket.strip() for bracket in brackets_list]

    for i in range(len(brackets_list)):
        if brackets_list[i] == "<" or brackets_list[i] == "<<":
            brackets_list[i] = "("
        elif brackets_list[i] == ">" or brackets_list[i] == ">>":
            brackets_list[i] = ")"

    for bracket in brackets_list:
        if bracket not in "()":
            return False

    if brackets_list[0]!= "(" or brackets_list[-1]!= ")":
        return False

    for i in range(len(brackets_list)):
        if brackets_list[i] == "(":
            brackets_list[i] = ">"
        elif brackets_list[i] == ")":
            brackets_list[i] = "<"

    for bracket in brackets_list:
        if bracket not in "()":
            return False

    return

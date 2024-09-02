

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
    brackets_list_copy = list(brackets)
    for i in range(len(brackets_list)):
        brackets_list[i] = ""
    brackets_list_copy.reverse()
    brackets_list.reverse()
    brackets_list = brackets_list + brackets_list_copy
    brackets_list = list(brackets_list)
    for i in range(len(brackets_list)):
        if brackets_list[i] == "<":
            brackets_list[i] = ">"
        elif brackets_list[i] == ">":
            brackets_list[i] = "<"
    brackets_string = ''.join(brackets_list)
    brackets_list = list(brackets_string)
    for i in range(len(brackets_list)):
        if brackets_list[i] == ">":
            brackets_list[i] = "<"
    brackets_list = list(brackets_string)
    for i in range

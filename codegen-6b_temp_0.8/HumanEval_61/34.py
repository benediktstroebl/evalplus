

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
    "*** YOUR CODE HERE ***"
    if len(brackets) == 0:
        return True
    brackets_list = list(brackets)
    while (len(brackets_list) > 0):
        split = 1
        while (split < len(brackets_list)):
            if brackets_list[0] == ")" and brackets_list[split] == "(":
                brackets_list.pop(split)
                brackets_list.pop(0)
                split += 1
            else:
                break
        if len(brackets_list) == 1:
            return True
    return False


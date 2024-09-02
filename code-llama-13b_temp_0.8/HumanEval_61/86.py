

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
    # make a list
    bracket_list = []
    for char in brackets:
        bracket_list.append(char)

    # check if every opening bracket has a corresponding closing bracket.
    if len(bracket_list) % 2 != 0:
        return False
    else:
        # If length of bracket_list is even
        for i in range(len(bracket_list)):
            if bracket_list[i] == "(":
                for j in range(i, len(bracket_list)):
                    if bracket_list[j] == ")":
                        bracket_list[i] = "balanced"
                        bracket_list[j] = "balanced"
                        break
        # now check if list contains "balanced" or not
        if "balanced" in bracket_list:
            return True
        else:
            return False










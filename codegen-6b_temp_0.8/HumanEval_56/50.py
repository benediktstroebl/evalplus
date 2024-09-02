

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
    # write a for loop to walk through each opening bracket
    # for each opening bracket, check if there is a corresponding closing bracket,
    # and then remove that closing bracket.
    # finally, check if there are any remaining opening brackets.
    # if there is, return False; else, return True.
    to_remove = []
    for i in range(len(brackets)):
        if brackets[i] == ">" and i != len(brackets) - 1:
            for j in range(len(brackets) - 1, i, -1):
                if brackets[j] == "<":
                    to_remove += [j] # add the index of the closing bracket
                elif brackets[j] == ">":
                    break
        if len(to_remove) > 0:
            for j in range(len(to_remove)):
                brackets = brackets[:to_remove[j]] + brackets[to_remove[j] + 1:]
            to_remove = []

    if len(brackets) > 0:
        return False
    else:
        return True





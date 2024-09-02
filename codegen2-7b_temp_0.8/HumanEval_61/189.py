

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
    brackets = brackets.replace("(", "").replace(")", "")
    correct = True
    for i in range(len(brackets)):
        if not brackets[i] == "(" and not brackets[i] == ")":
            correct = False
            break
    return



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
    # start = 0
    # openNum = []
    # closeNum = []

    # for i in range(len(brackets)):
    #     if brackets[i] == "(":
    #         openNum.append(i)
    #     elif brackets[i] == ")":
    #         closeNum.append(i)

    # for i in range(len(openNum)):
    #     if closeNum[i] - openNum[i] > 1:
    #         return False
    # return True

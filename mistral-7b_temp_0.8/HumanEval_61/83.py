

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

    brackets = brackets.replace("()", "")
    brackets = brackets.replace("()", "")
    brackets = brackets.replace("()", "")
    brackets = brackets.replace("()", "")
    if len(brackets) % 2 != 0:
        return False
    else:
        for i in range(len(brackets)):
            if brackets[i] == ')' and brackets[i - 1] == '(':
                brackets = brackets[0: i] + brackets[i + 1: len(brackets)]
            else:
                continue
    if len(brackets) == 0:
        return True
    else:
        return False





































































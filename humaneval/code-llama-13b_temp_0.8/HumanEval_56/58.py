

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
    brackets = list(brackets)
    for i in range(len(brackets)):
        if brackets[i] == "<":
            for j in range(i, len(brackets)):
                if brackets[j] == ">":
                    brackets[j] = "*"
                    break
            else:
                return False
    return all(bracket == "*" for bracket in brackets)




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
    if len(brackets) == 0:
        return True
    if len(brackets) % 2 != 0:
        return False

    if brackets[0] == ">":
        return False
    if brackets[-1] == "<":
        return False

    if brackets[0] == "<" and brackets[-1] == ">":
        return True

    # we only need to deal with odd number of brackets
    # every opening bracket has a corresponding closing bracket
    # v[0] = i
    # v[1] = j
    # v[2] = the number of the correct closing bracket
    # we count the number of each type of bracket
    v = [0 for _ in range(3)]

    for i in range(0, len(brackets)):
        if brackets[i] == "<":
            v[0] = i
        elif brackets[i] == ">":
            if v[0] == 0:
                return False
            else:
                v[2] += 1
                if v[1] == i - v[0] - 1:
                    v[1] = i
                    v[0] = -1
                elif v[1] < i - v[0] - 1:
                    v[1] = i

    if v[0] != -1 or v[2] % 2 != 0:
        return False
    else:
        return True


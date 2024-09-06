

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
    i, j = 0, len(brackets) - 1
    stack = []

    while i < j:
        while i < len(brackets) and brackets[i] != ">":
            i += 1

        while j >= 0 and brackets[j] != "<":
            j -= 1

        if i == j and brackets[i] == ">":
            return False
        i += 1
        j -= 1
        if i < j:
            stack.append(i)
            i += 1
        elif i == j:
            if len(stack) == 0:
                return False
            elif brackets[i] == "<" and brackets[j] == ">":
                return False
            elif brackets[i] != ">" or brackets[j] != "<":
                return False
            else:
                stack.pop()
                i += 1
                j -= 1

    return len(stack) == 0


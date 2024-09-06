

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
    # Your code here
    i = 0
    while i < len(brackets):
        if brackets[i] == '<':
            found = False
            for j in range(i+1, len(brackets)):
                if brackets[j] == '>':
                    found = True
                    break
            if not found:
                return False
            else:
                i = j
        else:
            i += 1
    return True





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

    
    brackets = "".join(brackets)
    count_open = 0
    count_close = 0
    stack = []

    for i in range(len(brackets)):
        if brackets[i] == '<':
            count_open += 1
        if brackets[i] == '>':
            count_close += 1

        if count_open - count_close == 0:
            continue

        if count_open - count_close!= 0:
            stack.append(brackets[i])
    
    if count_open!= count_close or stack:
        return False

    return True


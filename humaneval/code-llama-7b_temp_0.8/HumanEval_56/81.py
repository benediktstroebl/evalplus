

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
    # L = [i for i in brackets if i=='<']
    # R = [i for i in brackets if i=='>']
    # print(L, R)
    # return len(L)==len(R)

    # return all(brackets[i] == brackets[-i - 1]
    #            for i in range(len(brackets) // 2))
    l_counter = 0
    r_counter = 0
    for bracket in brackets:
        if bracket == '<':
            l_counter += 1
        if bracket == '>':
            r_counter += 1
        if l_counter == r_counter:
            return True
    return False


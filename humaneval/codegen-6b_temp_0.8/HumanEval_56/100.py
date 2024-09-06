

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
    opening_brackets = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            opening_brackets.append(i)
        elif brackets[i] == ">":
            if opening_brackets:
                del opening_brackets[-1]
            else:
                return False
    return len(opening_brackets) == 0

import doctest
doctest.testmod()


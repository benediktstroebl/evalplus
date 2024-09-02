

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
    # return True
    # return False
    # if brackets == '()':
    #     return True
    # if brackets[0] == '(':
    #     return False
    # return correct_bracketing(brackets[1:])

    # get rid of all the '(' in brackets
    # if no opening bracket left, all the remaining ')' should be paired.
    # if there are still '(', not paired ones left, return False
    # return True

    # we can also use recursion
    # if brackets == '':
    #     return True
    # if brackets[0] == '(':
    #     return False
    # if brackets[-1] == ')':
    #     return False
    # return correct_bracketing(brackets[1:-1])

    # if not brackets:
    #     return True
    # if brackets[0] != '(':
    #     return False
    # if brackets[-1] != ')':
    #     return False
    # return correct_bracketing(brackets[1:-1])

    # if brackets == '':
    #     return True
    # if brackets[0] != '(':
    #     return False
    # return correct_bracketing(brackets[1:])

    if brackets == '':
        return True
    if brackets[0] != '(':
        return False
    return correct_bracketing(brackets[1:])


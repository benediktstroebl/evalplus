

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

    # Note: the following two expressions are equivalent:
    #      (brackets[0] == '(' and brackets[-1] == ')')
    #      '()'.startswith('(') and '()'.endswith(')')
    return brackets.startswith('(') and brackets.endswith(')') and ''.join(correct_bracketing_helper(brackets[1:-1])) == ''


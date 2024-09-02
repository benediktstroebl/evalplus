

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
    brackets = brackets.split(' ')

    def not_in_the_middle_of_the_pair(pair):
        return not (pair[0] in brackets and pair[1] in brackets)

    return not any(not_in_the_middle_of_the_pair(pair) for pair in zip(brackets[:-1],brackets[1:]))




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

    # step 1: write a recursive function to check that each
    #         bracket has a corresponding closing bracket.

    # step 2: return True or False according to the answer of the recursive function.

    # Hint: what is the base case?

    return recursive_bracket_checker(brackets, 0)





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
    # Return True if every opening bracket has a corresponding closing bracket.
    # The first step is to look for pairs of brackets that match.
    # For example, in the string "()" we will see one "(" and one ")".
    # This is a pair that matches, so we should return True.
    #
    # When we look for pairs of brackets, we will look for an opening bracket
    # and its corresponding closing bracket.
    # An opening bracket is "(" and a closing bracket is ")".
    #
    # Here is a list of opening brackets and closing brackets:
    # ["(", ")", "{", "}", "[", "]"]
    #
    # Here is an example of how we can find the first pair of matching brackets:
    #
    # Let's look at the string "(()())".
    #
    # We will check the indexes of the first "(" and the first ")".
    # The index of the first "(" is 0, and the index of the first ")" is 5.
    #
    #

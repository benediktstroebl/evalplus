

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
    bracket_map = (
        "()",
        "(()",
        ")()",
        "())(",
    )
    brackets = list(brackets)
    # create a list of all the starting and ending indices of the brackets
    bracket_indices = []
    for i, bracket in enumerate(brackets):
        if bracket == "(":
            bracket_indices.append(i)
        elif bracket == ")":
            try:
                bracket_indices.remove(i)
            except ValueError:
                print(bracket_indices, i)
                return False
    # If the bracket_indices are empty, then there are no opened and closed brackets
    if not bracket_indices:
        return True
    # If there are any opening brackets which are not closed, then the string is not balanced
    for i in bracket_indices:
        # If there is a closing bracket not found, then the string is not balanced
        if i < bracket_indices[0]:
            print(bracket_indices)
            return False
        # If there are no closed brackets, then the string is not balanced
        elif bracket_indices.count(i) > 1:
            return False
    return True

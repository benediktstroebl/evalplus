

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

    # First, determine if parentheses are balanced. If they aren't, return False.
    balanced = check_balanced(brackets)
    if not balanced:
        return False

    # Else, start at the beginning and keep track of how many closing brackets you've seen.
    # If the number of closing brackets is equal to the number of opening brackets,
    # we've got a valid string of parentheses.
    count = 0
    for char in brackets:
        if char == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True

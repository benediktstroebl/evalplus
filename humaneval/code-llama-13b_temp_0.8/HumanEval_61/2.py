

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

    # Keep track of the number of opening brackets.
    # If the number ever goes negative, it means there
    # are too many closing brackets.
    bracket_count = 0

    # Loop over each character in brackets.
    for bracket in brackets:
        if bracket == '(':
            # Found an opening bracket, so increase the count.
            bracket_count += 1
        else:
            # Found a closing bracket, so decrease the count.
            bracket_count -= 1

        # If our count every becomes negative, we have too many closing brackets
        # (the loop will continue going over the remaining characters, but we know
        # that it's not balanced so we can just return False early.)
        if bracket_count < 0:
            return False

    # If our count is not zero, we have more opening brackets than closing brackets
    # (and again, we know that it's not balanced so we can just return False.)
    if bracket_count != 0:
        return False

    # We haven't found any problems, so return True!
    return True




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
    open_to_closed = {"(": ")", ")": "("}
    # Keep track of number of open brackets we've seen.
    num_open = 0
    # for each bracket in the string
    for bracket in brackets:
        # If it's an opening bracket, increment the counter.
        if bracket == "(":
            num_open += 1
        # If it's a closing bracket
        elif bracket == ")":
            # if the counter is zero, we have too many closing brackets.
            if num_open == 0:
                return False
            # otherwise decrement the counter.
            else:
                num_open -= 1
    # If we ever reach the end and the counter is still nonzero, we have too many opening brackets.
    if num_open > 0:
        return False
    # Otherwise, all brackets were balanced.
    return True



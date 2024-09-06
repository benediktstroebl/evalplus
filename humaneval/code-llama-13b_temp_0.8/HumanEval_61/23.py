

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
    # Hint: Keep track of the number of opening brackets - call it num_open.
    # Increment num_open every time you see an opening bracket.
    # Decrement num_open every time you see a closing bracket.
    # Initially num_open = 0
    # After processing all characters, if num_open is 0,
    # then the bracketing was correct.
    num_open = 0
    for b in brackets:
        if b == '(':
            num_open += 1
        else:
            num_open -= 1
            if num_open < 0:
                return False
    return num_open == 0

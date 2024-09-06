

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

    # Hint 1: remember the concept of "stack".

    # Hint 2: use a while loop to check the condition, the length of string
    # could be reduced.

    # Hint 3: don't forget to return the result.

    # Time complexity O(n)
    if len(brackets) % 2 != 0:
        return False
    open_cnt = 0
    for b in brackets:
        if b == '(':
            open_cnt += 1
        elif b == ')':
            open_cnt -= 1
            if open_cnt < 0:
                return False
    return True


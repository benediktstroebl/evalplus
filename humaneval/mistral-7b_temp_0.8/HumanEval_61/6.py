

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
    brackets = brackets.strip()
    opening_brackets = "([{"
    closing_brackets = "])]}"
    opening_brackets_len = len(opening_brackets)
    closing_brackets_len = len(closing_brackets)
    counter = 0
    for bracket in brackets:
        if bracket in opening_brackets:
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                return False
    if counter > 0:
        return False
    return True


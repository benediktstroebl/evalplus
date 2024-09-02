

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
    def count_open(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
        return count

    def count_close(s):
        count = 0
        for c in s:
            if c == ')':
                count += 1
        return count

    open_counts = {c: count_open(brackets) for c in brackets}
    close_counts = {c: count_close(brackets) for c in brackets}

    for c in brackets:
        if open_counts[c] != close_counts[c]:
            return False
    return True

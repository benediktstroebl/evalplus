

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

    open_brackets = [0]
    for c in brackets:
        if c == "(":
            open_brackets.append(0)
        else:
            open_brackets[-1] += 1
    if len(open_brackets) == 1:
        return True
    close_brackets = open_brackets[:]
    close_brackets.pop()
    brackets_pairs = zip(open_brackets, close_brackets)
    for opening, closing in brackets_pairs:
        if closing > opening:
            return False
    return True
    

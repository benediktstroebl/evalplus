

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
    brackets = brackets.replace(" ", "")
    if len(brackets) % 2 == 1:
        return False
    if len(brackets) == 0:
        return True
    open_brackets = brackets[0]
    close_brackets = brackets[-1]
    for i in range(len(brackets)//2):
        if open_brackets!= close_brackets:
            return False
        open_brackets = brackets[i]
        close_brackets = brackets[-1-i

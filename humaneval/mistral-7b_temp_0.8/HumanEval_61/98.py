

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
    open_brackets = []
    for char in brackets:
        if char == "(":
            open_brackets.append(char)
        else:
            if len(open_brackets) > 0 and open_brackets[-1] == "(":
                open_brackets.pop()
            else:
                return False
    return len(open_brackets) == 0

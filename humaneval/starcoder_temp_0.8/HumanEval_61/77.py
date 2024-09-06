

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
    assert isinstance(brackets, str), "brackets must be a string."
    result = True

    open_brackets = []
    for char in brackets:
        if char == "(":
            open_brackets.append(char)
        if char == ")":
            if open_brackets:
                open_brackets.pop()
            else:
                result = False
                break

    if open_brackets:
        result = False

    return result

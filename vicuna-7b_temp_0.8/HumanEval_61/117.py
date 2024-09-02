

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
    # use a set to keep track of the open brackets
    open_brackets = set()
    # iterate through the string of brackets
    for char in brackets:
        if char == "(":
            open_brackets.add(char)
        elif char == ")":
            if open_brackets.remove(char) != None:
                return False
    return True

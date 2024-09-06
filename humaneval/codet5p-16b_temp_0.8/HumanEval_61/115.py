

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

    opening_brackets = []
    for char in brackets:
        if char == "(":
            opening_brackets.append(char)
        elif char == ")":
            if not opening_brackets:
                return False
            opening_brackets.pop()

    return len(opening_brackets) == 0

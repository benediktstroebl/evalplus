

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

    open_bracket = "("
    close_bracket = ")"

    opening_brackets = []
    closing_brackets = []

    for i in range(len(brackets)):
        if brackets[i] == open_bracket:
            opening_brackets.append(i)

        if brackets[i] == close_bracket:
            closing_brackets.append(i)

    for i in opening_brackets:
        if i not in closing_brackets:
            return False
        closing_brackets.remove(i)

    return True


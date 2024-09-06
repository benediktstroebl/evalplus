

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
    closed_brackets = []
    for index, bracket in enumerate(brackets):
        if bracket == "(":
            opening_brackets.append(index)
        elif bracket == ")":
            # pop off the opening bracket if it's the last opening bracket
            if opening_brackets:
                opened_index = opening_brackets.pop()
                closed_brackets.append((opened_index, index))
            else:
                return False

    return closed_brackets == []


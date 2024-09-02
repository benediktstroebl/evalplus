

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
    brackets = brackets.replace("(", "").replace(")", "")
    if brackets == "":
        return True

    opening_brackets = brackets[::2]
    closing_brackets = brackets[1::2]

    return all(closing_brackets[i] == opening_brackets[i] for i in range(len(closing_brackets)))

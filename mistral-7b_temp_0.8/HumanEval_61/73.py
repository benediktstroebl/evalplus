

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
    brackets = brackets.replace("(", "[")
    brackets = brackets.replace(")", "]")
    brackets = brackets.replace("(", "(")
    brackets = brackets.replace(")", ")")
    brackets = list(brackets)
    if brackets[0] == "[" and brackets[-1] == "]":
        return True
    else:
        return False


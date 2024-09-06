

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
    if len(brackets) == 0:
        return True
    else:
        if brackets[0] == ")" or brackets[-1] == "(":
            return False
        else:
            return correct_bracketing(brackets[1:len(brackets)-1])

assert correct_bracketing("(") == False
assert correct_bracketing("()") == True
assert correct_bracketing("(()())") == True
assert correct_bracketing(")(()") == False

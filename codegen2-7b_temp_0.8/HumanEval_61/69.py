

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
    brackets = brackets.strip()
    if len(brackets) % 2!= 0:
        return False
    opening_brackets = ["(", "{"]
    closing_brackets = [")", "}"]
    for bracket in brackets:
        if bracket not in opening_brackets and bracket not in closing_brackets:
            return False
    return

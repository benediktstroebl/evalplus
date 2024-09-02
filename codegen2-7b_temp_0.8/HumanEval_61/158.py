

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
    s = brackets.replace("(", "").replace(")", "").replace(" ", "")
    if s == "":
        return True
    open_brackets = set(s)
    for i in range(len(s)):
        if s[i] == "(":
            open_brackets.remove(")")
        if s[i] == ")":
            return False
    return len(open_brackets) == 0

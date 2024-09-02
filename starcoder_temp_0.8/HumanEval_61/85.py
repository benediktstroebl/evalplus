

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

    st = []
    for c in brackets:
        if c == "(":
            st.append(c)
        elif c == ")":
            if not st:
                return False
            st.pop()
    return st == []

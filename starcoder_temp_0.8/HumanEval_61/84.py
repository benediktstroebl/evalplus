

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
    # Your code here
    st = []
    for i in brackets:
        if i == "(":
            st.append(i)
        elif i == ")":
            if st and st[-1] == "(":
                st.pop()
            else:
                return False
    if not st:
        return True
    else:
        return False




def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    "*** YOUR CODE HERE ***"
    st = []
    for b in brackets:
        if b == "<":
            st.append(b)
        elif b == ">" and st:
            st.pop()
        else:
            return False
    return True if not st else False


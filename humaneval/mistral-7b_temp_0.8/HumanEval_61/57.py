

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

    # check if there are any opening brackets at all
    if "(" not in brackets:
        return False

    # Initialize stack
    s = []
    for b in brackets:
        if b == '(':
            s.append(b)
        elif b == ')':
            # if the stack is empty, or the first character in the stack is '(',
            # then the brackets are unbalanced
            if not s or s[0] != '(':
                return False
            # otherwise, pop the first character from the stack
            s.pop(0)
    # return True if the stack is empty at the end
    return not s


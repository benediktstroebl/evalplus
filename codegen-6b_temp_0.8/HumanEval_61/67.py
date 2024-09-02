

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
    ans = True
    stack = Stack()
    for c in brackets:
        if c == "(":
            stack.push("(")
        else:
            if c == ")":
                if stack.is_empty() or not stack.pop() == "(":
                    ans = False
                    break
    return ans and stack.is_empty()
            
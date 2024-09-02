

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

    open_brackets = ["(", "[", "{"]
    close_brackets = [")", "]", "}"]
    stack = []
    for bracket in brackets:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackets:
            if not stack:
                return False
            if open_brackets.index(stack.pop())!= close_brackets.index(bracket):
                return False
    return True if not stack else False



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
    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]
    stack = Stack()
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.push(bracket)
        else:
            if not stack.is_empty():
                top = stack.pop()
                if top!= bracket:
                    return False
    return stack.is_empty()

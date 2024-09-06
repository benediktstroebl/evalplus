

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
    open_brackets = ["(", "[", "{", "<"]
    close_brackets = [")", "]", "}", ">"]
    stack = []
    for char in brackets:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if stack == []:
                return False
            stack.pop()
    return len(stack) ==

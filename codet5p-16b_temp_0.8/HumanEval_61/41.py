

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
    brackets_list = list(brackets)
    brackets_stack = []
    for br in brackets_list:
        if br in opening_brackets:
            brackets_stack.append(br)
        elif br in closing_brackets:
            if len(brackets_stack) == 0:
                return False
            if closing_brackets.index(br)!= opening_brackets.index(brackets_stack.pop()):
                return False
    return True if len(brackets_stack) == 0 else False


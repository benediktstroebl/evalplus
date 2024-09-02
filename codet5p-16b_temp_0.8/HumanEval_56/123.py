

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

    open_brackets = ">"
    close_brackets = "<"
    open_brackets_stack = []

    for bracket in brackets:
        if bracket in open_brackets:
            open_brackets_stack.append(bracket)
        elif bracket in close_brackets:
            if len(open_brackets_stack) == 0:
                return False
            else:
                open_bracket = open_brackets_stack.pop()
                if open_bracket!= close_brackets[open_brackets_stack.pop()]:
                    return False
    return len(open_brackets_stack) == 0

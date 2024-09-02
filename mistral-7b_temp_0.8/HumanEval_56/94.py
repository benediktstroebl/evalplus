

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
    opening_brackets = {"<", "["}
    closing_brackets = {">", "]"}
    brackets_stack = []
    for bracket in brackets:
        if bracket in opening_brackets:
            brackets_stack.append(bracket)
        elif bracket in closing_brackets:
            if not brackets_stack:
                return False
            else:
                bracket_to_pop = brackets_stack.pop()
                if bracket_to_pop in opening_brackets:
                    if bracket_to_pop != bracket:
                        return False
                else:
                    if bracket_to_pop != closing_brackets[closing_brackets.index(bracket)]:
                        return False

    if brackets_stack:
        return False
    else:
        return True


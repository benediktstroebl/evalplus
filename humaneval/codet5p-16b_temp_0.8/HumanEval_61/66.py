

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

    open_brackets = "({["
    close_brackets = ")}]"
    map_brackets = dict(zip(open_brackets, close_brackets))
    bracket_list = [map_brackets[b] for b in brackets]
    if len(bracket_list) == 0:
        return True

    stack = [bracket_list[0]]
    for bracket in bracket_list[1:]:
        if stack[-1] == bracket:
            stack.pop()
        else:
            stack.append(bracket)

    return len(stack) == 0


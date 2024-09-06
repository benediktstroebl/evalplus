

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

    brackets_stack = []
    bracket_pairs = {'<': '>', '{': '}', '(': ')'}

    for bracket in brackets:
        if bracket in bracket_pairs:
            brackets_stack.append(bracket)
        else:
            if not brackets_stack:
                return False
            current_bracket = brackets_stack.pop()
            if current_bracket!= bracket_pairs[current_bracket]:
                return False

    return len(brackets_stack) == 0



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
    # A stack is a list of pairs, where the first element is the item on the top
    # of the stack and the second element is the item on the bottom.
    stack = []
    bracket_pairs = {"(": ")", "{": "}", "[": "]"}
    for bracket in brackets:
        if bracket in bracket_pairs:
            stack.append(bracket_pairs[bracket])
            continue
        if not stack:
            return False
        if stack[-1] != bracket:
            return False
        stack.pop()
    return (stack == [])

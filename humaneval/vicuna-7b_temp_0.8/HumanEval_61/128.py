

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
    def find_bracket(brackets):
        for char in brackets:
            if char == "(":
                yield "(", 1
            elif char == ")":
                yield ")", 0

    def check_brace_match(match):
        if match[0] != match[1]:
            return False
        return True

    for opening_brace, closing_brace in find_bracket(brackets):
        if not any(check_brace_match(match) for match in zip(opening_brace, closing_brace)):
            return False
    return True

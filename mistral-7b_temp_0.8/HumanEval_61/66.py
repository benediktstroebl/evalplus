

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
    if len(brackets) % 2 != 0:
        return False
    brackets_length = len(brackets)
    opening_brackets_count = brackets.count("(")
    if opening_brackets_count != (brackets_length - opening_brackets_count):
        return False
    for bracket in brackets:
        if bracket == "(":
            counter = 0
            for bracket2 in brackets:
                if bracket2 == ")":
                    counter += 1
            if counter > 1:
                return False
    return True

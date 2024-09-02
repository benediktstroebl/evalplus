

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
    if not brackets:
        return False

    # remove trailing and leading parentheses
    brackets = brackets.lstrip("(")
    brackets = brackets.rstrip(")")

    # find opening brackets
    open_brackets = set(brackets)

    # find closing brackets
    close_brackets = set()

    for i in range(len(open_brackets)):
        for j in range(i + 1, len(open_brackets)):
            if open_brackets[i] == open_brackets[j]:
                # if opening brackets match, add them to close_brackets
                close_brackets.add(open_brackets[i])
            else:
                # if opening brackets do not match, return False
                return False

    # if all opening brackets have corresponding closing brackets, return True
    return all(close_brackets.difference({open_brackets[i] for i in range(len(open_brackets))}) in close_brackets for open_brackets in open_brackets)
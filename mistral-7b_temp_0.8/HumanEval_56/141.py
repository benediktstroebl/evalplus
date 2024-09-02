

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
    """
    opening_brackets = {
        '(',
        '{',
        '[',
        '<'
    }
    closing_brackets = {
        ')',
        '}',
        ']',
        '>'
    }
    """
    open_brackets = {
        '(',
        '{',
        '[',
        '<'
    }
    close_brackets = {
        ')',
        '}',
        ']',
        '>'
    }
    # brackets = "> < > < >"
    brackets = brackets.replace("  ", "")
    brackets = brackets.replace("  ", "")
    brackets = brackets.replace("  ", "")

    count = 0
    for bracket in brackets:
        if bracket in open_brackets:
            count += 1
        elif bracket in close_brackets:
            if count == 0:
                return False
            count -= 1
    return count == 0



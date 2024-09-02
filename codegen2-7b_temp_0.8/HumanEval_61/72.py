

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
    opening_bracket_to_closing = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    stack = []
    for i in brackets:
        if i in opening_bracket_to_closing:
            stack.append(i)
        else:
            if stack == []:
                return False
            if stack.pop()!= opening_bracket_to_closing[i]:
                return False
    

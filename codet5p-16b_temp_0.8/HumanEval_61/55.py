

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

    
    bracket_map = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    opening_brackets = bracket_map.keys()
    closing_brackets = bracket_map.values()
    stack = []
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if len(stack) == 0:
                return False
            elif stack[-1]!= bracket_map[stack[-1]]:
                return False
            else:
                stack.pop()
    return len(stack) == 0
    

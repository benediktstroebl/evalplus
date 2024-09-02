

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
    brackets_list = list(brackets)
    opening_brackets = [")", "("]
    closing_brackets = ["]", "[", "}"]
    stack = []
    for bracket in brackets_list:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if stack:
                if stack[-1] == bracket[:-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        elif bracket in opening_brackets + closing_brackets:
            return False
    return not stack


























































































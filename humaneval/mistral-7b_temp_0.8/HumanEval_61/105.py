

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

    opening_brackets = '({['
    closing_brackets = ')}]'

    if len(brackets) % 2 == 1:
        return False
    else:
        stack = []

        for bracket in brackets:
            if bracket in opening_brackets:
                stack.append(bracket)
            elif bracket in closing_brackets:
                if not stack:
                    return False
                else:
                    last_bracket = stack.pop()
                    if closing_brackets.index(bracket) == opening_brackets.index(last_bracket):
                        pass
                    else:
                        return False
            else:
                pass
        return not stack

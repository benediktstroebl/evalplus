

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

    opening = set(["(", "{", "["])
    closing = set(")", "}", "]")

    open_stack = []

    for bracket in brackets:
        if bracket in opening:
            open_stack.append(bracket)
        elif bracket in closing:
            if len(open_stack) == 0:
                return False
            if open_stack.pop() != bracket:
                return False
    return len(open_stack) == 0

assert correct_bracketing("(") == False
assert correct_bracketing("()") == True
assert correct_bracketing("(()())") == True
assert correct_bracketing(")(()") == False
assert correct_bracketing("()())") == True

